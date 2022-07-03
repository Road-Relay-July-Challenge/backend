import requests
from time import time
from flask import Blueprint, request
from server.routes import LIST_ALL_INDIVIDUAL, GET_HALL_OF_FAME, UPDATE_INDIVIDUAL_TOTAL_MILEAGE,ACTIVITIES_URL
from server.config import EVENT_END_TIME_OBJECT, EVENT_START_TIME_OBJECT
from server.db import get_data, get_mileages, get_users_sorted_by_mileage, update_data, update_mileage_data, update_multiple_datas, update_multiple_mileage_datas
from server.utils import get_new_access_token, convert_from_greenwich_to_singapore_time, get_week_from_date_object, logger, return_json

individual_api = Blueprint('individual_api', __name__)

@individual_api.route(LIST_ALL_INDIVIDUAL, methods=['GET'])
def list_all_individual():
    name_list = get_users_sorted_by_mileage()
    # filter to remove token fields
    users = []
    for user in name_list:
        to_add = {
            "athlete_id": user.get("athlete_id"),
            "name": user.get("name"),
            "team_number": user.get("team_number"),
            "total_contributed_mileage": user.get("total_contributed_mileage"),
            "total_true_mileage": user.get("total_true_mileage"),
            "multiplier": user.get("multiplier")
        }

        users.append(to_add)
    return return_json(True, "Successfully retrieved all individuals.", users)

@individual_api.route(GET_HALL_OF_FAME, methods=['GET'])
def get_hall_of_fame():
    # get top 5 individuals for longest run, furthest run, highest accmulated mileage
    # each a different function from DBs
    return

@individual_api.route(UPDATE_INDIVIDUAL_TOTAL_MILEAGE, methods=['POST'])
def update_individual_total_mileage():
    athlete_id = request.form.get('athlete_id')
    if athlete_id == None:
        return return_json(False, f"Missing athlete_id in request.")

    response = update_individual_weekly_mileage_from_strava(athlete_id)
    if "success" in response:
        return return_json(False, f"Error in updating mileage from Strava.", response)

    new_mileage_object = update_individual_total_mileage_from_db(athlete_id)
    person_mileage_object = {
        "athlete_id": athlete_id,
        "mileage": new_mileage_object
    }

    return return_json(True, f"Successfully updated {athlete_id}'s total mileage.", person_mileage_object)

def update_individual_weekly_mileage_from_strava(athlete_id):
    person = get_data(athlete_id)

    access_token_expiry = int(person.get("access_token_expired_at"))
    name = person.get("name")
    if access_token_expiry <= time():
        logger(f"{name}'s token expired at {access_token_expiry}. Refreshing...")
        obj = get_new_access_token(person.get("refresh_token"), name)
        if not isinstance(obj, str):
            return return_json(
                False, 
                f"Failed to refresh token from Strava.",
                obj
            )
        
        access_token = obj
    else:
        access_token = person.get("access_token")

    headers = {
            "Authorization": "Bearer " + access_token
    }
    activityRequest = requests.get(ACTIVITIES_URL, headers=headers)
    if activityRequest.status_code != 200:
        return return_json(
            False, 
            f"Failed to retrieve activities from Strava.\n Error code: {activityRequest.status_code}",
            activityRequest.json()
        )
    
    activityList = activityRequest.json()
    weekly_mileage_dict = {}
    for activity in activityList:
        greenwich_time_string = activity.get('start_date')
        sg_time_object = convert_from_greenwich_to_singapore_time(greenwich_time_string, "%Y-%m-%dT%H:%M:%SZ")
        if sg_time_object < EVENT_START_TIME_OBJECT or sg_time_object > EVENT_END_TIME_OBJECT:
            continue

        if activity.get('type') != 'Run':
            continue

        week = get_week_from_date_object(sg_time_object)
        if week in weekly_mileage_dict:
            weekly_mileage_dict[week] = weekly_mileage_dict[week] + activity.get('distance')
        else:
            weekly_mileage_dict[week] = activity.get('distance')

    multiplier = person.get("multiplier")
    for week in weekly_mileage_dict:
        to_update = {
            "true_mileage": round(int(weekly_mileage_dict[week]) / 1000, 2),
            "contributed_mileage": round(int(weekly_mileage_dict[week] * multiplier) / 1000, 2)
        }
        update_multiple_mileage_datas(athlete_id, week, to_update)

    return weekly_mileage_dict

def update_individual_total_mileage_from_db(athlete_id):
    total_true_mileage = 0
    total_contributed_mileage = 0
    
    mileages = get_mileages(athlete_id)
    for week in mileages: 
        total_true_mileage = total_true_mileage + week.get("true_mileage")
        total_contributed_mileage = total_contributed_mileage + week.get("contributed_mileage") + week.get("special_mileage")
    
    mileage_object = {
        "total_true_mileage": total_true_mileage,
        "total_contributed_mileage": total_contributed_mileage
    }
    update_multiple_datas(athlete_id, mileage_object)

    return mileage_object