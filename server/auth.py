from flask import Blueprint, request, redirect
from time import time
import requests
import urllib3
from server.config import AUTH_URL, CLIENT_ID, CLIENT_SECRET, EAST_WEST_REDIRECT_URL, EAST_WEST_SIGN_UP_END_TIME_OBJECT, EVENT_WEEKS
from server.routes import AUTHORIZE_EAST_WEST, CHOOSE_EAST_OR_WEST, REFRESH_ALL_EAST_WEST, VERIFY, OAUTH_URL, REFRESH_ALL, AUTHORIZE
from server.individual import update_individual_east_west_mileage_from_strava
from server.utils import return_json, logger
from server.db import add_mileages, add_person, add_user_rank, get_all_east_west_users, get_users_sorted_by_mileage, is_person_added, is_side_added, update_multiple_datas, add_side

auth_api = Blueprint('auth_api', __name__)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # disables insecure request warning for verify

@auth_api.route(AUTHORIZE, methods=['GET'])
def authorize():
    return redirect(AUTH_URL)

@auth_api.route(VERIFY, methods=['GET'])
def verify():
    args = request.args
    authorizationCode = args.get('code')
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': authorizationCode,
        'grant_type': 'authorization_code'
    }
    response = requests.post(OAUTH_URL, data=payload, verify=False)
    if response.status_code != 200:
        return return_json(False, f"Failed to retrieve athlete.", response.json())
    response = response.json()
    
    person = {
        "name": response.get('athlete').get('firstname') + " " + response.get('athlete').get('lastname'),
        "athlete_id": response.get('athlete').get('id'),
        "access_token": response.get('access_token'),
        "access_token_expired_at": response.get('expires_at'),
        "refresh_token": response.get("refresh_token"),
        "team_number" : 0,
        "total_true_mileage" : 0,
        "total_contributed_mileage": 0,
        "multiplier": 1,
        "longest_run": 0,
        "total_time_spent": 0
    }
    if is_person_added(person["athlete_id"]):
        logger(f"{person['name']} tried to verify again.")
        return return_json(True, f"You have already been verified, {person['name']}.", None)

    add_person(person)
    logger(f"Successfully added {person['name']}.")

    add_user_rank(person['athlete_id'])
    logger(f"Successfully initialized {person['name']}'s ranking.")

    for week in EVENT_WEEKS:
        mileages = {
            "athlete_id": response.get('athlete').get('id'),
            "week": week,
            "true_mileage": 0,
            "contributed_mileage": 0,
            "special_mileage": 0 
        }
        add_mileages(mileages)

    logger(f"Successfully initialized {person['name']}'s mileages.")
    return return_json(True, f"Welcome to RRJC 2022, {person['name']}.", [person, mileages])

@auth_api.route(AUTHORIZE_EAST_WEST, methods=['GET'])
def authorize_east_west():
    chosen_side = request.args.get("chosen_side")
    EAST_WEST_URL = f"https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={EAST_WEST_REDIRECT_URL}&response_type=code&scope=activity:read_all&state={chosen_side}"
    return redirect(EAST_WEST_URL)

@auth_api.route(CHOOSE_EAST_OR_WEST, methods=['GET'])
def choose_east_or_west():
    authorizationCode = request.args.get('code')
    chosen_side = request.args.get("chosen_side")
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': authorizationCode,
        'grant_type': 'authorization_code'
    }
    response = requests.post(OAUTH_URL, data=payload, verify=False)
    if response.status_code != 200:
        return return_json(False, f"Failed to retrieve athlete.", response.json())
    response = response.json()
    
    athlete_id = response.get('athlete').get('id')
    name = response.get('athlete').get('firstname') + " " + response.get('athlete').get('lastname'),
    person = {
        "access_token": response.get('access_token'),
        "access_token_expired_at": response.get('expires_at'),
        "refresh_token": response.get("refresh_token"),
    }

    if not is_person_added(athlete_id):
        logger(f"{person['name']} not registered before.")
        return return_json(True, f"You have never been verified. Go on to the Register page to verify once first.", None)

    update_multiple_datas(athlete_id, person)

    if time() > EAST_WEST_SIGN_UP_END_TIME_OBJECT:
        return return_json(True, f"It is past the registration deadline for the event.", None)

    if is_side_added(athlete_id):
        return return_json(True, f"You have already chosen your side. We don't do betrayals here.", None)

    if chosen_side not in ["east", "west"]:
        return return_json(False, f"Side not chosen. Got {chosen_side} instead.", None)

    add_side(athlete_id, name[0], chosen_side)

    logger(f"Successfully added {name[0]}'s side, {chosen_side}.")
    return return_json(True, f"Successfully added your chosen side, the great {chosen_side.upper()}", None)
    