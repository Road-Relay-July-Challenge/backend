from flask import Blueprint, request, redirect
import requests
import urllib3
from server.config import AUTH_URL, CLIENT_ID, CLIENT_SECRET, EAST_WEST_REDIRECT_URL, EVENT_WEEKS
from server.routes import VERIFY, OAUTH_URL, REFRESH_ALL, AUTHORIZE
from server.individual import update_individual_total_mileage_from_db, update_individual_weekly_mileage_from_strava
from server.team import update_all_team_mileage
from server.utils import return_json, logger
from server.db import add_mileages, add_person, get_users_sorted_by_mileage, is_person_added, is_side_added, update_multiple_datas, add_side

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
    }
    if is_person_added(person["athlete_id"]):
        logger(f"{person['name']} tried to verify again.")
        return return_json(True, f"You have already been verified, {person['name']}.", None)

    add_person(person)
    logger(f"Successfully added {person['name']}")

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

@auth_api.route(REFRESH_ALL, methods=['POST'])
def refresh_all():
    athletes_and_team_number = get_users_sorted_by_mileage()

    for athlete in athletes_and_team_number:
        obj = update_individual_weekly_mileage_from_strava(athlete.get("athlete_id"))
        if not isinstance(obj, dict):
            return obj

        obj = update_individual_total_mileage_from_db(athlete.get("athlete_id"))
        mileage = obj
        name = athlete.get("name")
        logger(f"Successfully updated {name}'s mileage. {mileage}")
    
    update_all_team_mileage()
    return return_json(True, f"Successfully refreshed all teams' and individuals.", None)

@auth_api.route("/authorize_east_west", methods=['GET'])
def authorize_east_west():
    chosen_side = request.args.get("chosen_side")
    EAST_WEST_URL = f"https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={EAST_WEST_REDIRECT_URL}&response_type=code&scope=activity:read_all&state={chosen_side}"
    return redirect(EAST_WEST_URL)

@auth_api.route("/choose_east_or_west", methods=['GET'])
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
    person = {
        "access_token": response.get('access_token'),
        "access_token_expired_at": response.get('expires_at'),
        "refresh_token": response.get("refresh_token"),
    }

    if not is_person_added(athlete_id):
        logger(f"{person['name']} not registered before.")
        return return_json(False, f"You have never been verified. Go on to the Register page to verify once first.", None)

    update_multiple_datas(athlete_id, person)

    if is_side_added(athlete_id):
        return return_json(False, f"You have already chosen your side. We don't do betrayals here.", None)

    if (chosen_side is not "east") and (chosen_side is not "west"):
        return return_json(False, f"Side not chosen. Got {chosen_side} instead.", None)

    add_side(athlete_id, chosen_side)

    logger(f"Successfully added {athlete_id}'s side, {chosen_side}.")
    return return_json(True, f"Successfully added your chosen side, the great {chosen_side.upper()}", None)
    