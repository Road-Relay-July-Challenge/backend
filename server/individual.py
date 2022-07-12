import requests
from time import time
from flask import Blueprint, request
from server.routes import ADD_ALL_USER_RANKINGS, GET_USER_RANKINGS, LIST_ALL_INDIVIDUAL, GET_HALL_OF_FAME, UPDATE_INDIVIDUAL_TOTAL_MILEAGE,ACTIVITIES_URL, UPDATE_USER_RANKINGS
from server.config import EAST_WEST_EVENT_END_TIME_OBJECT, EAST_WEST_EVENT_START_TIME_OBJECT, EVENT_END_TIME_OBJECT, EVENT_START_TIME_OBJECT, LIMIT_PER_CATEGORY, MAX_MILEAGE_FOR_TIER_2_RUNS, MAX_MILEAGE_FOR_TIER_3_RUNS, MAX_NUMBER_OF_TIER_2_RUNS, SLOWEST_ALLOWABLE_PACE
from server.db import add_user_rank, get_data, get_mileage_of_week, get_mileages, get_user_rankings_in_db, get_users_sorted_by_category_and_limit, get_users_sorted_by_mileage, update_east_west_mileage, update_multiple_datas, update_multiple_mileage_datas, update_user_rankings_in_db
from server.utils import get_new_access_token, convert_from_greenwich_to_singapore_time, get_week_from_date_object, logger, return_json

individual_api = Blueprint('individual_api', __name__)

@individual_api.route(LIST_ALL_INDIVIDUAL, methods=['GET'])
def list_all_individual():
    name_list = get_users_sorted_by_mileage()
    # filter to remove token fields
    # convert to km
    users = []
    for user in name_list:
        to_add = {
            "athlete_id": user.get("athlete_id"),
            "name": user.get("name"),
            "team_number": user.get("team_number"),
            "total_contributed_mileage": user.get("total_contributed_mileage") / 1000,
            "total_true_mileage": user.get("total_true_mileage") / 1000,
            "multiplier": user.get("multiplier"),
            "longest_run": user.get("longest_run") / 1000,
            "total_time_spent": user.get("total_time_spent"),
        }

        users.append(to_add)

    logger("Successfully retrieved all individuals.")
    return return_json(True, "Successfully retrieved all individuals.", users)

@individual_api.route(GET_HALL_OF_FAME, methods=['GET'])
def get_hall_of_fame():
    # get top 5 individuals for longest run, furthest run, highest accmulated mileage
    # each a different function from DBs
    list_dict = {}

    list_dict['highest_contributed_mileage_list'] = get_users_sorted_by_category_and_limit("total_contributed_mileage", LIMIT_PER_CATEGORY)
    list_dict['highest_true_mileage_list'] = get_users_sorted_by_category_and_limit("total_true_mileage", LIMIT_PER_CATEGORY)
    list_dict['longest_run_list'] = get_users_sorted_by_category_and_limit("longest_run", LIMIT_PER_CATEGORY)
    list_dict['longest_time_spent_list'] = get_users_sorted_by_category_and_limit("total_time_spent", LIMIT_PER_CATEGORY)

    # filter to remove token fields
    for athlete_list in list_dict:
        temp_list = []
        for user in list_dict[athlete_list]:
            to_add = {
                "athlete_id": user.get("athlete_id"),
                "name": user.get("name"),
                "team_number": user.get("team_number"),
                "total_contributed_mileage": user.get("total_contributed_mileage"),
                "total_true_mileage": user.get("total_true_mileage"),
                "multiplier": user.get("multiplier")
            }

            temp_list.append(to_add)
        list_dict[athlete_list] = temp_list

    hall_of_fame = {
        "Highest Contributed Mileage": list_dict['highest_contributed_mileage_list'],
        "Highest True Mileage": list_dict['highest_true_mileage_list'],
        "Longest Run": list_dict['longest_run_list'],
        "Longest Time Spent": list_dict['longest_time_spent_list']
    }

    return return_json(True, f"Successfully retrieved hall of fame.", hall_of_fame)

@individual_api.route(ADD_ALL_USER_RANKINGS, methods=['POST'])
def add_all_user_rankings():
    current_rank = 1
    user_list = get_users_sorted_by_mileage()
    for user in user_list:
        new_entry = add_user_rank(user['athlete_id'], current_rank)
        logger(f"Successfully added {user['name']} into rankings. {new_entry}")
        current_rank = current_rank + 1

    return return_json(True, "Successfully added all rankings.", None)

@individual_api.route(GET_USER_RANKINGS, methods=['GET'])
def get_user_rankings():
    rankings = get_user_rankings_in_db()

    logger(f"Successfully retrieved all user rankings. {rankings}")
    return return_json(True, "Successfully retrieved all user rankings.", rankings)

@individual_api.route(UPDATE_USER_RANKINGS, methods=['POST'])
def update_user_rankings():
    user_list = get_users_sorted_by_mileage()
    new_rankings = update_user_rankings_in_db(user_list)

    logger(f"Successfully updated user rankings. {new_rankings}")
    return return_json(True, "Successfully updated user rankings.", new_rankings)

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

    logger(f"Successfully updated {athlete_id}'s total mileage.", person_mileage_object)
    return return_json(True, f"Successfully updated {athlete_id}'s total mileage.", person_mileage_object)

def update_individual_weekly_mileage_from_strava(athlete_id):
    person = get_data(athlete_id)

    access_token_expiry = int(person.get("access_token_expired_at"))
    name = person.get("athlete_id")
    if access_token_expiry <= time():
        logger(f"{name}'s token expired at {access_token_expiry}. Refreshing...")
        obj = get_new_access_token(person.get("refresh_token"), athlete_id)
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
    longest_run = 0
    total_time_spent = 0
    for activity in activityList:
        greenwich_time_string = activity.get('start_date')
        sg_time_object = convert_from_greenwich_to_singapore_time(greenwich_time_string, "%Y-%m-%dT%H:%M:%SZ")
        if sg_time_object < EVENT_START_TIME_OBJECT or sg_time_object > EVENT_END_TIME_OBJECT:
            continue

        if activity.get('type') != 'Run':
            continue

        if activity.get('average_speed') < SLOWEST_ALLOWABLE_PACE:
            continue

        activity_distance = activity.get('distance')
        longest_run = longest_run if activity_distance <= longest_run else activity_distance
        total_time_spent = total_time_spent + activity.get('moving_time')

        week = get_week_from_date_object(sg_time_object)
        if week in weekly_mileage_dict:
            weekly_mileage_dict[week].append(activity_distance)
        else:
            weekly_mileage_dict[week] = []
            weekly_mileage_dict[week].append(activity_distance)

    to_update = {
        "total_time_spent": total_time_spent,
        "longest_run": longest_run
    }
    update_multiple_datas(athlete_id, to_update)

    multiplier = person.get("multiplier")
    for week in weekly_mileage_dict:
        athlete = get_mileage_of_week(athlete_id, week)
        special_mileage = athlete["special_mileage"]
        true_mileage = sum(weekly_mileage_dict[week])
        contributed_mileage = calculate_weekly_capped_mileage(weekly_mileage_dict[week])
        to_update = {
            "true_mileage": true_mileage,
            "contributed_mileage": contributed_mileage * multiplier + special_mileage
        }
        update_multiple_mileage_datas(athlete_id, week, to_update)

    return weekly_mileage_dict

def calculate_weekly_capped_mileage(mileage_list):
    capped_mileage = 0
    mileage_list = sorted(mileage_list, reverse=True)
    is_tier_1_run_factored = False
    max_number_of_tier_2_runs = MAX_NUMBER_OF_TIER_2_RUNS
    max_mileage_for_tier_2_runs = MAX_MILEAGE_FOR_TIER_2_RUNS
    max_mileage_for_tier_3_runs = MAX_MILEAGE_FOR_TIER_3_RUNS 
    for mileage in mileage_list:
        # highest uncapped run
        if not is_tier_1_run_factored:
            capped_mileage = capped_mileage + mileage
            is_tier_1_run_factored = True
        # next 3 highest runs capped at 12km
        elif is_tier_1_run_factored and max_number_of_tier_2_runs > 0:
            capped_mileage = capped_mileage + (mileage if mileage <= max_mileage_for_tier_2_runs else max_mileage_for_tier_2_runs)
            max_number_of_tier_2_runs = max_number_of_tier_2_runs - 1
        # all subsequent runs capped at 4km
        else:
            capped_mileage = capped_mileage + (mileage if mileage <= max_mileage_for_tier_3_runs else max_mileage_for_tier_3_runs)

    return capped_mileage

def update_individual_total_mileage_from_db(athlete_id):
    total_true_mileage = 0
    total_contributed_mileage = 0
    
    mileages = get_mileages(athlete_id)
    for week in mileages: 
        total_true_mileage = total_true_mileage + week.get("true_mileage")
        total_contributed_mileage = total_contributed_mileage + week.get("contributed_mileage")
    
    mileage_object = {
        "total_true_mileage": total_true_mileage,
        "total_contributed_mileage": total_contributed_mileage
    }
    update_multiple_datas(athlete_id, mileage_object)

    return mileage_object

def update_individual_east_west_mileage_from_strava(athlete_id):
    person = get_data(athlete_id)

    access_token_expiry = int(person.get("access_token_expired_at"))
    name = person.get("athlete_id")
    if access_token_expiry <= time():
        logger(f"{name}'s token expired at {access_token_expiry}. Refreshing...")
        obj = get_new_access_token(person.get("refresh_token"), athlete_id)
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
    # weekly_mileage_dict = {}
    total_mileage = 0
    for activity in activityList:
        greenwich_time_string = activity.get('start_date')
        sg_time_object = convert_from_greenwich_to_singapore_time(greenwich_time_string, "%Y-%m-%dT%H:%M:%SZ")
        if sg_time_object < EAST_WEST_EVENT_START_TIME_OBJECT or sg_time_object > EAST_WEST_EVENT_END_TIME_OBJECT:
            continue

        if activity.get('type') != 'Run':
            continue

        if activity.get('average_speed') < SLOWEST_ALLOWABLE_PACE:
            continue

        total_mileage = total_mileage + activity.get('distance')

    multiplier = person.get("multiplier")
    total_mileage = total_mileage * multiplier
        
    update_east_west_mileage(athlete_id, total_mileage)

    return total_mileage
