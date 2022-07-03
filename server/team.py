from flask import Blueprint
from server.routes import LIST_ALL_TEAM, UPDATE_ALL_TEAM_MILEAGE
from server.db import get_sorted_teams, get_users_sorted_by_mileage, update_multiple_datas, update_multiple_team_datas
from server.utils import return_json

team_api = Blueprint('team_api', __name__)

@team_api.route(LIST_ALL_TEAM, methods=['GET'])
def list_all_team():
    team_list = get_sorted_teams()
    return return_json(True, "Successfully retrieved all teams.", team_list)

@team_api.route(UPDATE_ALL_TEAM_MILEAGE, methods=['POST'])
def update_team_mileage():
    all_users = get_users_sorted_by_mileage()
    team_dict = {}
    for user in all_users:
        current_team_id = user.get("team_number")
        print(current_team_id)
        if current_team_id in team_dict:
            team_dict[current_team_id]["team_true_mileage"] = team_dict[current_team_id]["team_true_mileage"] + user.get("total_true_mileage")
            team_dict[current_team_id]["team_contributed_mileage"] = team_dict[current_team_id]["team_contributed_mileage"] + user.get("total_contributed_mileage")
        else:
            team_dict[current_team_id] = {}
            team_dict[current_team_id]["team_true_mileage"] = user.get("total_true_mileage")
            team_dict[current_team_id]["team_contributed_mileage"] = user.get("total_contributed_mileage")

    for team in team_dict:
        update_multiple_team_datas(team, team_dict[team])

    return return_json(True, "Successfully updated all teams' mileage.", team_dict)