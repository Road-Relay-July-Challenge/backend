from flask import Blueprint
from routes import LIST_ALL_TEAM

team_api = Blueprint('team_api', __name__)

@team_api.route(LIST_ALL_TEAM)
def list_all_team():
    # get sorted array from DB
    # return as json -> use jsonify()
    return 
