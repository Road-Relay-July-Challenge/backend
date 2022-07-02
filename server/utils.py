import requests
from datetime import datetime, timedelta
from flask import jsonify
from config import CLIENT_ID, CLIENT_SECRET
from routes import OAUTH_URL
from db import update_multiple_datas

def logger(message):
    print(f"[{datetime.now()}] {message}")

def return_json(is_success, return_message, result_object):
    return jsonify(
        success=is_success,
        message=return_message,
        result=result_object
    )

def get_new_access_token(refresh_token, name):
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }

    response = requests.post(OAUTH_URL, data=payload, verify=False)
    if response.status_code != 200:
        return response.json()
    logger(f"{name}'s token refreshed. New expiry: {response.json()['expires_at']}")

    new_tokens = {
        "access_token": response.json()['access_token'],
        "refresh_token": response.json()['refresh_token'],
        "access_token_expired_at": int(response.json()['expires_at'])
    }
    update_multiple_datas(name, new_tokens)
    
    return response.json()['access_token']

def convert_from_greenwich_to_singapore_time(timestring, format):
    greenwich_time = datetime.strptime(timestring, format)
    sg_time_object = greenwich_time + timedelta(hours=8)

    return sg_time_object