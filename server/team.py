from flask import Blueprint
from server.routes import GET_ALL_EAST_WEST_MILEAGE, LIST_ALL_TEAM, UPDATE_ALL_TEAM_MILEAGE
from server.db import get_all_east_west_users, get_sorted_teams, get_users_sorted_by_mileage, update_multiple_team_datas
from server.utils import return_json, logger

team_api = Blueprint('team_api', __name__, url_prefix='/team')

@team_api.route(LIST_ALL_TEAM, methods=['GET'])
def list_all_team():
    team_list = get_sorted_teams()
    logger("Successfully retrieved all teams.")
    return return_json(True, "Successfully retrieved all teams.", team_list)

@team_api.route(UPDATE_ALL_TEAM_MILEAGE, methods=['POST'])
def update_all_team_mileage():
    all_users = get_users_sorted_by_mileage()
    team_dict = {}
    for user in all_users:
        current_team_id = user.get("team_number")
        if current_team_id in team_dict:
            team_dict[current_team_id]["team_true_mileage"] = team_dict[current_team_id]["team_true_mileage"] + user.get("total_true_mileage")
            team_dict[current_team_id]["team_contributed_mileage"] = team_dict[current_team_id]["team_contributed_mileage"] + user.get("total_contributed_mileage")
        else:
            team_dict[current_team_id] = {}
            team_dict[current_team_id]["team_true_mileage"] = user.get("total_true_mileage")
            team_dict[current_team_id]["team_contributed_mileage"] = user.get("total_contributed_mileage")

    for team in team_dict:
        update_multiple_team_datas(team, team_dict[team])
        logger(f"Successfully updated team {team}'s mileage. {team_dict[team]}")

    logger("Successfully updated all teams' mileage.")
    return return_json(True, "Successfully updated all teams' mileage.", team_dict)

@team_api.route(GET_ALL_EAST_WEST_MILEAGE, methods=['GET'])
def get_all_east_west_mileage():
    user_list = get_all_east_west_users()
    east_side_pax = 0
    east_side_mileage = 0
    west_side_pax = 0
    west_side_mileage = 0

    for user in user_list:
        if user.get("chosen_side") == "east":
            east_side_pax = east_side_pax + 1
            east_side_mileage = east_side_mileage + user.get("mileage")
        elif user.get("chosen_side") == "west":
            west_side_pax = west_side_pax + 1
            west_side_mileage = west_side_mileage + user.get("mileage")

    to_return = {
        "user_list": user_list,
        "east_side_pax": east_side_pax,
        "east_side_mileage": east_side_mileage,
        "west_side_pax": west_side_pax,
        "west_side_mileage": west_side_mileage,
    }

    logger(f"Successfully retrieved all east west mileages.")
    return return_json(True, f"Successfully retrieved all east west mileages.", to_return)
