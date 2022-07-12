from server.auth import refresh_all, refresh_all_east_west
from server.db import update_refresh_time
from app import app

if __name__ == "__main__":
    with app.app_context():
        refresh_all()
        refresh_all_east_west()
        update_refresh_time()