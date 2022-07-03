import os
from dotenv import load_dotenv
import datetime

load_dotenv('.env')

DEBUG = True
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
CLIENT_REFRESH_TOKEN = os.environ.get("CLIENT_REFRESH_TOKEN")

# event time objects
EVENT_START_TIME_OBJECT = datetime.datetime.strptime("2022-07-04 00:00:00", "%Y-%m-%d %H:%M:%S")
EVENT_END_TIME_OBJECT = datetime.datetime.strptime("2022-07-23 23:59:59", "%Y-%m-%d %H:%M:%S")
START_WEEK = EVENT_START_TIME_OBJECT.isocalendar()[1]
END_WEEK = EVENT_END_TIME_OBJECT.isocalendar()[1]
EVENT_WEEKS = []
counter = START_WEEK
while counter <= END_WEEK:
    EVENT_WEEKS.append(counter)
    counter = counter + 1

# db
DB_TYPE = "service_account"
DB_PROJECT_ID = os.environ.get("DB_PROJECT_ID")
DB_PRIVATE_KEY_ID = os.environ.get("DB_PRIVATE_KEY_ID")
DB_PRIVATE_KEY = os.environ.get("DB_PRIVATE_KEY").replace('\\n', '\n')
DB_CLIENT_EMAIL = os.environ.get("DB_CLIENT_EMAIL")
DB_CLIENT_ID = os.environ.get("DB_CLIENT_ID")
DB_AUTH_URI = "https://accounts.google.com/o/oauth2/auth"
DB_TOKEN_URI = "https://oauth2.googleapis.com/token"
DB_AUTH_PROVIDER_X509_CERT_URL = "https://www.googleapis.com/oauth2/v1/certs"
DB_CLIENT_X509_CERT_URL = os.environ.get("DB_CLIENT_X509_CERT_URL")
