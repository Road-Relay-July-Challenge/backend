from flask import Blueprint
from server.routes import ADD_ALL_TEAM_RANKINGS, GET_ALL_EAST_WEST_MILEAGE, GET_TEAM_RANKINGS, LIST_ALL_TEAM, UPDATE_ALL_TEAM_MILEAGE, UPDATE_TEAM_RANKINGS
from server.db import add_team_rank, get_all_east_west_users, get_sorted_teams, get_team_rankings_in_db, get_users_sorted_by_mileage, update_multiple_team_datas, update_team_rankings_in_db
from server.utils import return_json, logger

team_api = Blueprint('team_api', __name__, url_prefix='/team')

@team_api.route(LIST_ALL_TEAM, methods=['GET'])
def list_all_team():
    team_list = get_sorted_teams()
    for team in team_list:
        team['team_true_mileage'] = team['team_true_mileage'] / 1000
        team['team_contributed_mileage'] = team['team_contributed_mileage'] / 1000
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

    east_side_list = []
    east_side_pax = 0
    east_side_mileage = 0
    west_side_list = []
    west_side_pax = 0
    west_side_mileage = 0

    for user in user_list:
        user['mileage'] = user['mileage'] / 1000
        if user.get("chosen_side") == "east":
            east_side_list.append(user)
            east_side_pax = east_side_pax + 1
            east_side_mileage = east_side_mileage + user.get("mileage")
        elif user.get("chosen_side") == "west":
            west_side_list.append(user)
            west_side_pax = west_side_pax + 1
            west_side_mileage = west_side_mileage + user.get("mileage")

    to_return = {
        "east_side_list": east_side_list,
        "west_side_list": west_side_list,
        "east_side_pax": east_side_pax,
        "east_side_mileage": east_side_mileage / 1000,
        "west_side_pax": west_side_pax,
        "west_side_mileage": west_side_mileage / 1000,
    }

    logger(f"Successfully retrieved all east west mileages.")
    return return_json(True, f"Successfully retrieved all east west mileages.", to_return)

@team_api.route(ADD_ALL_TEAM_RANKINGS, methods=['POST'])
def add_all_team_rankings():
    current_rank = 1
    team_list = get_sorted_teams()
    for team in team_list:
        new_entry = add_team_rank(team['team_id'], current_rank)
        logger(f"Successfully added {team['team_id']} into rankings. {new_entry}")
        current_rank = current_rank + 1

    return return_json(True, "Successfully added all rankings.", None)

@team_api.route(GET_TEAM_RANKINGS, methods=['GET'])
def get_team_rankings():
    rankings = get_team_rankings_in_db()

    logger(f"Successfully retrieved all team rankings. {rankings}")
    return return_json(True, "Successfully retrieved all team rankings.", rankings)

@team_api.route(UPDATE_TEAM_RANKINGS, methods=['POST'])
def update_team_rankings():
    team_list = get_sorted_teams()
    new_rankings = update_team_rankings_in_db(team_list)

    logger(f"Successfully updated team rankings. {new_rankings}")
    return return_json(True, "Successfully updated team rankings.", new_rankings)