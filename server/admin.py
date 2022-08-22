from flask import Blueprint
from server.db import add_user_into_achievement, get_all_east_west_users, get_all_users, get_sorted_teams_by_id, get_users_sorted_by_mileage
from server.individual import update_individual_east_west_mileage_from_strava, update_individual_total_mileage_from_db, update_individual_weekly_mileage_from_strava

from server.routes import ADD_ALL_USERS_INTO_ACHIEVEMENTS_COLLECTION, REFRESH_ALL, REFRESH_ALL_EAST_WEST
from server.team import update_all_team_mileage
from server.utils import logger, return_json

admin_api = Blueprint('admin_api', __name__, url_prefix='/admin')

@admin_api.route(ADD_ALL_USERS_INTO_ACHIEVEMENTS_COLLECTION, methods=['POST'])
def add_all_users_into_achievements_collection():
    user_list = get_all_users()
    team_list = get_sorted_teams_by_id()
    for user in user_list:
        to_set = {
            "athlete_id": user['athlete_id'],
            "name": user['name'],
            "achievement_count": 0,
            "team_id": user['team_number'],
            "team_name": team_list[user['team_number'] - 1]["team_name"],
            "rewarded_mileage": 0
        }

        add_user_into_achievement(to_set)
        
        logger(f"Successfully added {user['name']} into Achievements collection.")

    logger("Successfully added all users into achievements collection.")
    return return_json(True, "Successfully added all users into achievements collection.", None)

@admin_api.route(REFRESH_ALL, methods=['POST'])
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
    return return_json(True, f"Successfully refreshed all teams and individuals.", None)

@admin_api.route(REFRESH_ALL_EAST_WEST, methods=['POST'])
def refresh_all_east_west():
    athletes_and_side = get_all_east_west_users()
    east_side_mileage = 0
    east_side_pax = 0
    west_side_mileage = 0
    west_side_pax = 0

    for athlete in athletes_and_side:
        mileage = update_individual_east_west_mileage_from_strava(athlete["athlete_id"])
        if not isinstance(mileage, int) and not isinstance(mileage, float):
            return return_json(False, f"Unable to get mileage of {athlete['name']}", mileage)

        chosen_side = athlete.get("chosen_side")
        if chosen_side == "east":
            east_side_mileage = east_side_mileage + mileage
            east_side_pax = east_side_pax + 1
        elif chosen_side == "west":
            west_side_mileage = west_side_mileage + mileage
            west_side_pax = west_side_pax + 1

        logger(f"Successfully updated {athlete['name']}'s mileage to {mileage} km.")

    logger("Successfully refreshed all for east and west.")
    return return_json(True, "Successfully refreshed all for east and west.", None)
