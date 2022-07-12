from flask import Blueprint
from server.db import add_user_into_achievement, get_all_users

from server.routes import ADD_ALL_USERS_INTO_ACHIEVEMENTS_COLLECTION
from server.utils import logger, return_json

admin_api = Blueprint('admin_api', __name__, url_prefix='/admin')

@admin_api.route(ADD_ALL_USERS_INTO_ACHIEVEMENTS_COLLECTION, methods=['POST'])
def add_all_users_into_achievements_collection():
    user_list = get_all_users()
    for user in user_list:
        to_set = {
            "athlete_id": user['athlete_id'],
            "name": user['name'],
            "achievement_count": 0
        }

        add_user_into_achievement(to_set)
        
        logger(f"Successfully added {user['name']} into Achievements collection.")

    logger("Successfully added all users into achievements collection.")
    return return_json(True, "Successfully added all users into achievements collection.", None)
