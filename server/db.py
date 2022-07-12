from firebase_admin import credentials, firestore, initialize_app
import server.config as config
from time import time

from server.utils import convert_seconds_to_hours_minutes_seconds_string

cred = credentials.Certificate(
    {
        "type": config.DB_TYPE,
        "project_id": config.DB_PROJECT_ID,
        "private_key_id": config.DB_PRIVATE_KEY_ID,
        "private_key": config.DB_PRIVATE_KEY,
        "client_email": config.DB_CLIENT_EMAIL,
        "client_id": config.DB_CLIENT_ID,
        "auth_uri": config.DB_AUTH_URI,
        "token_uri": config.DB_TOKEN_URI,
        "auth_provider_x509_cert_url": config.DB_AUTH_PROVIDER_X509_CERT_URL,
        "client_x509_cert_url": config.DB_CLIENT_X509_CERT_URL
    }
)
initialize_app(cred)
db = firestore.client()

#testing stuff
def test():
    user_id = 'zhen hong'
    doc_ref = db.collection('Users').document(user_id)
    doc_ref.set({
        'Name':'zhen hong',
        'Age' : 21
    })

def get_refresh_time():
    time_ref = db.collection('System_configs').document("last_refresh").get()
    return time_ref

def update_refresh_time():
    doc_ref = db.collection('System_configs').document("last_refresh")
    new_refresh_time = time()
    doc_ref.update({
        "last_refresh_time": new_refresh_time
    })

    return new_refresh_time

def is_person_added(athlete_id):
    person_ref = db.collection('Users').document(str(athlete_id)).get()
    return person_ref.exists

#take in a dictionary and adds person to database with specified fields
def add_person(person):
    doc_ref = db.collection('Users').document(str(person.get("athlete_id")))
    doc_ref.set({
        "name" : person.get("name"),
        "athlete_id" : person.get("athlete_id"),
        "access_token" : person.get("access_token"),
        "access_token_expired_at" : person.get("access_token_expired_at"),
        "refresh_token" : person.get("refresh_token"),
        "team_number" : person.get("team_number"),
        "total_true_mileage" : person.get("total_true_mileage"),
        "total_contributed_mileage": person.get("total_contributed_mileage"),
        "multiplier": person.get("multiplier"),
        "longest_run": person.get("longest_run"),
        "total_time_spent": person.get("total_time_spent")
    })

def add_mileages(mileages):
    doc_ref = db.collection('Mileages').document(str(mileages.get("athlete_id")))
    doc_ref.set({
        "athlete_id": mileages.get("athlete_id")
    })

    doc_ref = db.collection('Mileages').document(str(mileages.get("athlete_id"))).collection('weeks').document(str(mileages.get("week")))
    doc_ref.set({
        "week": mileages.get("week"),
        "true_mileage": mileages.get("true_mileage"),
        "contributed_mileage": mileages.get("contributed_mileage"),
        "special_mileage": mileages.get("special_mileage") 
    })

def get_mileages(athlete_id):
    to_return = []
    weeks = db.collection('Mileages').document(str(athlete_id)).collection('weeks').stream()
    for week in weeks:
        to_return.append(week.to_dict())

    return to_return

def get_mileage_of_week(athlete_id, week):
    doc_ref = db.collection('Mileages').document(str(athlete_id)).collection('weeks').document(str(week))
    return doc_ref.get().to_dict()

#returns a list of all the names
def get_all_names():
    users = db.collection('Users').stream()
    names = []
    for user in users:
        names.append(user.to_dict()['name'])
    return names

def get_all_users():
    users = db.collection('Users').stream()
    all_users = []
    for user in users:
        all_users.append(user.to_dict())
    return all_users

#used to update any data. example to update refresh token to 12345, 
#field_name = 'access_token' and updated_data = '12345'
def update_data(athlete_id, field_name, updated_data):
    doc_ref = db.collection('Users').document(str(athlete_id))
    doc_ref.update({
        field_name : updated_data
    })

def update_multiple_datas(athlete_id, updated_data_obj):
    doc_ref = db.collection('Users').document(str(athlete_id))
    doc_ref.update(updated_data_obj)

def update_mileage_data(athlete_id, week, field_name, updated_data):
    doc_ref = db.collection('Mileages').document(str(athlete_id)).collection('weeks').document(str(week))
    doc_ref.update({
        field_name : updated_data
    })

def update_multiple_mileage_datas(athlete_id, week, updated_data_obj):
    doc_ref = db.collection('Mileages').document(str(athlete_id)).collection('weeks').document(str(week))
    doc_ref.update(updated_data_obj)

#get user's name using athlete id
def get_user_name(athlete_id):
    doc_ref = db.collection('Users').document(str(athlete_id))
    person_ref = doc_ref.get()
    return person_ref.to_dict()['name']

#get all data using athlete_id
def get_data(athlete_id):
    doc_ref = db.collection('Users').document(str(athlete_id))
    person_ref = doc_ref.get()
    name = person_ref.to_dict()['name']
    athlete_id = person_ref.to_dict()['athlete_id']
    access_token = person_ref.to_dict()['access_token']
    access_token_expired_at = person_ref.to_dict()['access_token_expired_at']
    refresh_token = person_ref.to_dict()['refresh_token']
    team_number = person_ref.to_dict()['team_number']
    total_true_mileage = person_ref.to_dict()["total_true_mileage"]
    total_contributed_mileage = person_ref.to_dict()["total_contributed_mileage"]
    multiplier = person_ref.to_dict()["multiplier"]
    longest_run = person_ref.to_dict()['longest_run']
    total_time_spent = person_ref.to_dict()['total_time_spent']
    
    weekly_mileages = []
    doc_ref = db.collection('Mileages').document(str(athlete_id)).collection('weeks').stream()
    for week in doc_ref:
        weekly_mileages.append(week.to_dict())

    person = {
        "name" : name,
        "athlete_id" : athlete_id,
        "access_token" : access_token,
        "access_token_expired_at" : access_token_expired_at,
        "refresh_token" : refresh_token,
        "team_number" : team_number,
        "total_true_mileage" : total_true_mileage,
        "total_contributed_mileage" : total_contributed_mileage,
        "multiplier": multiplier,
        "weekly_mileages": weekly_mileages,
        "longest_run": longest_run,
        "total_time_spent": total_time_spent
    }

    return person

def get_users_sorted_by_mileage():
    users_stream = db.collection('Users').stream()
    users = []
    for element in users_stream:
        users.append(element.to_dict())
    sorted_names = sorted(users, key=lambda d: d["total_contributed_mileage"], reverse = True)
    return sorted_names

def get_users_sorted_by_category_and_limit(category, limit):
    categories_with_mileage = ["longest_run", "total_contributed_mileage", "total_true_mileage"]
    categories_with_time = ["total_time_spent"]

    users_stream = db.collection('Users').stream()
    users = []
    for element in users_stream:
        athlete_id = element.to_dict()['athlete_id']
        name = element.to_dict()['name']
        team_number = element.to_dict()['team_number']
        data = element.to_dict()[category]
        if category in categories_with_mileage:
            data = round( (data / 1000), 2 )
        if category in categories_with_time:
            data = convert_seconds_to_hours_minutes_seconds_string(data)

        to_append = {
            "athlete_id": athlete_id,
            "name": name,
            "team_number": team_number,
            "data": data
        }

        users.append(to_append)

    sorted_names = sorted(users, key=lambda d: d["data"], reverse = True)
    
    if limit is not None:
        return sorted_names[:limit]
    return sorted_names

def update_achievement_data(athlete_id, field_name, updated_data):
    doc_ref = db.collection('Achievements').document(str(athlete_id))
    doc_ref.update({
        field_name: update_data
    })

############## TEAM FUNCTIONS ######################

def add_team(team):
    doc_ref = db.collection('Teams').document(str(team.get("team_id")))
    doc_ref.set({
        "team_id" : team.get("team_id"),
        "team_name" : team.get("team_name"),
        "team_mileage" : team.get("team_mileage")
    })


#used to update any team data
def update_team_data(team_id, field_name, updated_data):
    doc_ref = db.collection('Teams').document(str(team_id))
    doc_ref.update({
        field_name : updated_data
    })

def update_multiple_team_datas(team_id, update_obj):
    doc_ref = db.collection('Teams').document(str(team_id))
    doc_ref.update(update_obj)

def get_all_team_id():
    team_id = db.collection('Teams').stream()
    teams = []
    for team in team_id:
        teams.append(team.to_dict()['team_id'])
    return teams

def get_sorted_teams():
    teams = get_all_team_id()
    unsorted_teams = []
    for team in teams:
        doc_ref = db.collection('Teams').document(str(team))
        team_ref = doc_ref.get()
        team_name = team_ref.to_dict()['team_name']
        team_contributed_mileage = team_ref.to_dict()['team_contributed_mileage']
        team_true_mileage = team_ref.to_dict()['team_true_mileage']
        team_data = {
            "team_id" : team,
            "team_name": team_name,
            "team_contributed_mileage": team_contributed_mileage,
            "team_true_mileage": team_true_mileage
        }
        unsorted_teams.append(team_data)
    sorted_teams = sorted(unsorted_teams, key=lambda d: d["team_contributed_mileage"], reverse = True) 
    return sorted_teams

############## ADMIN FUNCTIONS ######################
def add_user_into_achievement(user_object):
    doc_ref = db.collection('Achievements').document(str(user_object['athlete_id']))
    doc_ref.set(user_object)

############## RANKING FUNCTIONS ########################

def add_user_rank(athlete_id, ranking=None):
    doc_ref = db.collection('User_rankings').document(str(athlete_id))
    new_entry = {
        "athlete_id": athlete_id,
        "current_rank": ranking if ranking is not None else 999,
        "last_refresh_rank": 999 
    }
    doc_ref.set(new_entry)

    return new_entry

def get_user_rankings_in_db():
    rankings_stream = db.collection('User_rankings').stream()
    rankings = []
    for user in rankings_stream:
        rankings.append(user.to_dict())
    return rankings

def update_user_rankings_in_db(user_list):
    new_rankings = []
    current_rank = 1
    collection_ref = db.collection('User_rankings')
    for user in user_list:
        person_ref = collection_ref.document(str(user['athlete_id']))
        new_last_refresh_rank = person_ref.get().to_dict()['current_rank']
        person_ref.update({
            "last_refresh_rank": new_last_refresh_rank,
            "current_rank": current_rank
        })

        current_rank = current_rank + 1
        new_rankings.append({"name": user['name'], "current_rank": current_rank, "last_refresh_rank": new_last_refresh_rank})
    
    return new_rankings

def add_team_rank(team_id, ranking=None):
    doc_ref = db.collection('Team_rankings').document(str(team_id))
    new_entry = {
        "athlete_id": team_id,
        "current_rank": ranking if ranking is not None else 999,
        "last_refresh_rank": 999 
    }
    doc_ref.set(new_entry)

    return new_entry

def get_team_rankings_in_db():
    rankings_stream = db.collection('Team_rankings').stream()
    rankings = []
    for team in rankings_stream:
        rankings.append(team.to_dict())
    return rankings

def update_team_rankings_in_db(team_list):
    new_rankings = []
    current_rank = 1
    collection_ref = db.collection('Team_rankings')
    for team in team_list:
        person_ref = collection_ref.document(str(team['team_id']))
        new_last_refresh_rank = person_ref.get().to_dict()['current_rank']
        person_ref.update({
            "last_refresh_rank": new_last_refresh_rank,
            "current_rank": current_rank
        })

        current_rank = current_rank + 1
        new_rankings.append({"name": team['team_id'], "current_rank": current_rank, "last_refresh_rank": new_last_refresh_rank})
    
    return new_rankings

############## EAST WEST CHALLENGE FUNCTIONS ######################

def is_side_added(athlete_id):
    return db.collection("East_or_west").document(str(athlete_id)).get().exists

def add_side(athlete_id, name, chosen_side):
    doc_ref = db.collection('East_or_west').document(str(athlete_id))
    doc_ref.set({
        "name": name,
        "athlete_id": athlete_id,
        "chosen_side": chosen_side,
        "mileage": 0
    })

def get_all_east_west_users():
    users_stream = db.collection('East_or_west').stream()
    users = []
    for element in users_stream:
        users.append(element.to_dict())
    sorted_names = sorted(users, key=lambda d: d["mileage"], reverse = True)

    return sorted_names

def update_east_west_mileage(athlete_id, mileage):
    doc_ref = db.collection('East_or_west').document(str(athlete_id))
    doc_ref.update({
        "mileage": mileage
    })

def main():
    #test()

    #sample data
    name = "jason"
    athlete_id = '179456'
    access_token = '123123'
    access_token_expired_at = '456456'
    refresh_token = '999'
    team_number = 2
    mileage = 0

    #can reuse this dictionary to add ppl
    person = {
        "name" : name,
        "athlete_id" : athlete_id,
        "access_token" : access_token,
        "access_token_expired_at" : access_token_expired_at,
        "refresh_token" : refresh_token,
        "team_number" : team_number,
        "mileage" : mileage
    }


    team_id = "3"
    team_name = "worst team"
    team_mileage = 99999
    sample_team = {
        "team_id" : team_id,
        "team_name" : team_name,
        "team_mileage" : team_mileage
    }

    #add_person(person)
    #update_mileage("wen feng", 1200)
    #get_all_names()
    #update_data("zhen hong", "athlete_id", "789123")
    #get_name('987654')
    #get_data("jason")
    #get_sorted_names()
    #add_team(sample_team)
    #update_team_data("3", "team_mileage", 3)
    #get_sorted_teams()
    #get_all_team_number()


if __name__ == "__main__":
    main()