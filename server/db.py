from firebase_admin import credentials, firestore, initialize_app
import server.config as config

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
        "multiplier": 1,
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
        "weekly_mileages": weekly_mileages
    }

    return person

def get_users_sorted_by_mileage():
    users_stream = db.collection('Users').stream()
    users = []
    for element in users_stream:
        users.append(element.to_dict())
    sorted_names = sorted(users, key=lambda d: d["total_contributed_mileage"], reverse = True)
    return sorted_names

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
        team_contributed_mileage = team_ref.to_dict()['team_contributed_mileage']
        team_true_mileage = team_ref.to_dict()['team_true_mileage']
        team_data = {
            "team_id" : team,
            "team_contributed_mileage" : team_contributed_mileage,
            "team_true_mileage": team_true_mileage
        }
        unsorted_teams.append(team_data)
    sorted_teams = sorted(unsorted_teams, key=lambda d: d["team_contributed_mileage"], reverse = True) 
    return sorted_teams





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