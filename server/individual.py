import requests
from flask import Blueprint, request
from routes import LIST_ALL_INDIVIDUAL, GET_HALL_OF_FAME, UPDATE_INDIVIDUAL_TOTAL_MILEAGE,ACTIVITIES_URL
from config import EVENT_END_TIME_OBJECT, EVENT_START_TIME_OBJECT
from utils import get_new_access_token, convert_from_greenwich_to_singapore_time

individual_api = Blueprint('individual_api', __name__)

@individual_api.route(LIST_ALL_INDIVIDUAL)
def list_all_individual():
    # get sorted array from DB
    # return as json -> use jsonify()
    return 

@individual_api.route(GET_HALL_OF_FAME)
def get_hall_of_fame():
    # get top 5 individuals for longest run, furthest run, highest accmulated mileage
    # each a different function from DBs
    return

@individual_api.route(UPDATE_INDIVIDUAL_TOTAL_MILEAGE)
def update_individual_total_mileage():
    name = request.args.get('name')
    new_mileage = get_total_mileage_from_strava(name)
    # update DB
    return str(new_mileage)

def get_total_mileage_from_strava(name):
    refresh_token = 123 # get refresh_token from DB, using athlete_id
    access_token = get_new_access_token(refresh_token)
    headers = {
        "Authorization": "Bearer " + access_token
    }
    activityList = requests.get(ACTIVITIES_URL, headers=headers).json()

    totalDistance = 0
    for activity in activityList:
        # check if activity is within event time
        greenwich_time_string = activity.get('start_date')
        sg_time_object = convert_from_greenwich_to_singapore_time(greenwich_time_string, "%Y-%m-%dT%H:%M:%SZ")
        if sg_time_object < EVENT_START_TIME_OBJECT or sg_time_object > EVENT_END_TIME_OBJECT:
            continue

        # check if activity is of run type
        if activity.get('type') != 'Run':
            continue

        totalDistance = totalDistance + activity.get('distance')

    return int(totalDistance / 1000)