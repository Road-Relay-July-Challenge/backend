from server.auth import refresh_all
from app import app

if __name__ == "__main__":
    with app.app_context():
        refresh_all()