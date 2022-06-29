from flask import Blueprint, request
import requests
import urllib3
from config import CLIENT_ID, CLIENT_SECRET
from routes import VERIFY, OAUTH_URL

auth_api = Blueprint('auth_api', __name__)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # disables insecure request warning for login

@auth_api.route(VERIFY)
def login():
    args = request.args
    authorizationCode = args.get('code')
    print("Authorization code:", authorizationCode)
    print("Client ID:", CLIENT_ID)
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': authorizationCode,
        'grant_type': 'authorization_code'
    }
    response = requests.post(OAUTH_URL, data=payload, verify=False)

    # add response.refresh_token, response.athlete.username, response.athlete.id into DB

    return response.json()
