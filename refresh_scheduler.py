from server.db import update_refresh_time
from app import app
from server.individual import update_user_rankings
from server.team import update_team_rankings

if __name__ == "__main__":
    with app.app_context():
        update_user_rankings()
        update_team_rankings()
        update_refresh_time()