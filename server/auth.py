from flask import Blueprint, request
import requests
import urllib3
from server.config import CLIENT_ID, CLIENT_SECRET
from server.routes import VERIFY, OAUTH_URL, REFRESH_ALL
from server.individual import update_individual_total_mileage_from_strava
from server.utils import return_json, logger
from server.db import add_person, get_all_team_number, update_team_data

auth_api = Blueprint('auth_api', __name__)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # disables insecure request warning for verify

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
    response = requests.post(OAUTH_URL, data=payload, verify=False).json()

    person = {
        "name": response.get('athlete').get('firstname') + " " + response.get('athlete').get('lastname'),
        "athlete_id": response.get('athlete').get('id'),
        "access_token": response.get('access_token'),
        "access_token_expired_at": response.get('expires_at'),
        "refresh_token": response.get("refresh_token"),
        "mileage": 0
    }

    add_person(person)
    logger(f"Successfully added {person['name']}")
    return return_json(True, f"Successfully added {person['name']}", person)

@auth_api.route(REFRESH_ALL, methods=['POST'])
def refresh_all():
    teamMileageDict = {}
    athletes_and_team_number = get_all_team_number()

    for athlete in athletes_and_team_number:
        obj = update_individual_total_mileage_from_strava(athlete.get("name"))
        if not isinstance(obj, int):
            return obj
        mileage = obj

        team_number = athlete.get("team_number")

        if team_number in teamMileageDict:
            teamMileageDict[team_number] = teamMileageDict[team_number] + mileage
        else:
            teamMileageDict[team_number] = mileage
    
    # for each team, if mileage of team != updated mileage, update DB
    for team_number in teamMileageDict.keys():
        if not isinstance(team_number, int):
            continue
        update_team_data(team_number, "mileage", teamMileageDict.get(team_number))
        
    logger("Successfully refreshed all teams' mileage")
    return return_json(True, f"Successfully refreshed all teams' mileage", teamMileageDict)
    