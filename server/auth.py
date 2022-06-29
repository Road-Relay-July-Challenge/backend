from flask import Blueprint, request
import requests
import urllib3
from config import CLIENT_ID, CLIENT_SECRET
from routes import VERIFY, OAUTH_URL, REFRESH_ALL
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
    return return_json(True, f"Successfully added {person['name']}")

@auth_api.route(REFRESH_ALL, methods=['GET'])
def refresh_all():
    # make dictionary of all team and mileage = 0 
    # get collection of all participants from DB
    # collection contains: participantID, mileage, teamID, refreshToken

    # for each participant, call strava API to obtain updated mileage, and update dictionary
        # if there is a change, update participant in DB 
    # mileage of team += updated mileage 
    
    # for each team, if mileage of team != updated mileage, update DB 
    return