import os
from dotenv import load_dotenv
import datetime

load_dotenv('.env')

DEBUG = True
PRINT_TIME_STAMP = True if os.environ.get("PRINT_TIME_STAMP") == 'True' else False
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
CLIENT_REFRESH_TOKEN = os.environ.get("CLIENT_REFRESH_TOKEN")
AUTH_REDIRECT_URL = "https://rrjc-web.vercel.app/redirect/exchange_token"
AUTH_URL = f"https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={AUTH_REDIRECT_URL}&response_type=code&scope=activity:read_all"
EAST_WEST_REDIRECT_URL = "https://rrjc-web.vercel.app/redirect_east_west/exchange_token"

# event time objects
EVENT_START_TIME_OBJECT = datetime.datetime.strptime("2022-07-04 00:00:00", "%Y-%m-%d %H:%M:%S")
EVENT_END_TIME_OBJECT = datetime.datetime.strptime("2022-07-22 23:59:59", "%Y-%m-%d %H:%M:%S")
START_WEEK = EVENT_START_TIME_OBJECT.isocalendar()[1]
END_WEEK = EVENT_END_TIME_OBJECT.isocalendar()[1]
EVENT_WEEKS = []
counter = START_WEEK
while counter <= END_WEEK:
    EVENT_WEEKS.append(counter)
    counter = counter + 1

# event rules
MAX_MILEAGE_FOR_TIER_2_RUNS = 12
MAX_NUMBER_OF_TIER_2_RUNS = 3
MAX_MILEAGE_FOR_TIER_3_RUNS = 4
SLOWEST_ALLOWABLE_PACE = float(1) / (float(8) * float(60) / float(1000))    # min/km -> m/s

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
