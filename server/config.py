import os
from dotenv import load_dotenv
import datetime

load_dotenv('.env')

DEBUG = True
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
CLIENT_REFRESH_TOKEN = os.environ.get("CLIENT_REFRESH_TOKEN")

EVENT_START_TIME_OBJECT = datetime.datetime.strptime("2022-06-24 00:00:00", "%Y-%m-%d %H:%M:%S")
EVENT_END_TIME_OBJECT = datetime.datetime.strptime("2022-07-23 23:59:59", "%Y-%m-%d %H:%M:%S")

# db
TYPE = "service_account"
PROJECT_ID = os.environ.get("PROJECT_ID")
PRIVATE_KEY_ID = os.environ.get("PRIVATE_KEY_ID")
PRIVATE_KEY = os.environ.get("PRIVATE_KEY").replace('\\n', '\n')
CLIENT_EMAIL = os.environ.get("CLIENT_EMAIL")
CLIENT_ID = os.environ.get("CLIENT_ID")
AUTH_URI = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URI = "https://oauth2.googleapis.com/token"
AUTH_PROVIDER_X509_CERT_URL = "https://www.googleapis.com/oauth2/v1/certs"
CLIENT_X509_CERT_URL = os.environ.get("CLIENT_X509_CERT_URL")
