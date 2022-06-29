from pickle import TRUE
from flask import Flask
from auth import auth_api
from config import DEBUG

<<<<<<< HEAD:main.py
=======
from firebase_admin import credentials
from firebase_admin import firestore

>>>>>>> 6c7217533ac0f122ba65c5fdaa1ef802eb62d450:server/app.py
app = Flask(__name__)
app.register_blueprint(auth_api, url_prefix='/auth')

@app.route("/")
def hello():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=DEBUG)