from flask import Blueprint, request
import requests
import urllib3
from config import CLIENT_ID, CLIENT_SECRET
from routes import VERIFY, OAUTH_URL, REFRESH_ALL
from individual import update_individual_total_mileage_from_strava
from utils import return_json
from db import add_person

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
    print(f"Successfully added {person['name']}")
    return return_json(True, f"Successfully added {person['name']}", person)

@auth_api.route(REFRESH_ALL, methods=['GET'])
def refresh_all():
    # make dictionary of all team and mileage = 0 
    teamMileageDict = {}

    # get collection of all participants from DB
    all_athletes = []
    # collection contains: participant_name, mileage, team_number, refresh_token
    for athlete in all_athletes:
        mileage = update_individual_total_mileage_from_strava(athlete.get("name"))
        team_number = athlete.get("team_number")

        if teamMileageDict.has_key(team_number):
            teamMileageDict[team_number] = teamMileageDict[team_number] + mileage
        else:
            teamMileageDict[team_number] = mileage
    
    # for each team, if mileage of team != updated mileage, update DB 
    for team in teamMileageDict.keys():
        # update_data()
        continue
    return
    