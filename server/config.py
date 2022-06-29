import os
import datetime

DEBUG = True
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
CLIENT_REFRESH_TOKEN = os.environ.get("CLIENT_REFRESH_TOKEN")

EVENT_START_TIME_OBJECT = datetime.datetime.strptime("2022-06-24 00:00:00", "%Y-%m-%d %H:%M:%S")
EVENT_END_TIME_OBJECT = datetime.datetime.strptime("2022-07-23 23:59:59", "%Y-%m-%d %H:%M:%S")