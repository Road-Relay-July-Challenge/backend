from server.auth import refresh_all
from server.db import update_refresh_time
from app import app

if __name__ == "__main__":
    with app.app_context():
        refresh_all()
        update_refresh_time()