import sys
import time
from datetime import datetime, timedelta
from flask import jsonify
from server.config import BASE_ACHIEVEMENT_MILEAGE, PER_ACHIEVEMENT_MILEAGE, PRINT_TIME_STAMP

def logger(message):
    if PRINT_TIME_STAMP:
        print(f"[{datetime.now()}] {message}")
    else: 
        print(f"{message}")
    sys.stdout.flush()

def return_json(is_success, return_message, result_object):
    return jsonify(
        success=is_success,
        message=return_message,
        result=result_object
    )

def convert_from_greenwich_to_singapore_time(timestring, format):
    greenwich_time = datetime.strptime(timestring, format)
    sg_time_object = greenwich_time + timedelta(hours=8)

    return sg_time_object

def get_week_from_date_object(date_object):
    return date_object.isocalendar()[1]

def convert_seconds_to_hours_minutes_seconds_string(n_seconds):
    return time.strftime("%H:%M:%S", time.gmtime(n_seconds))

def get_achievement_mileage_from_achievement_count(achievement_count):
    if achievement_count <= 0:
        return 0
    
    return (achievement_count - 1) * PER_ACHIEVEMENT_MILEAGE + BASE_ACHIEVEMENT_MILEAGE 