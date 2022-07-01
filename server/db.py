from firebase_admin import credentials, firestore, initialize_app
import config

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

#take in a dictionary and adds person to database with specified fields
def add_person(person):
    doc_ref = db.collection('Users').document(person.get("name"))
    doc_ref.set({
        "name" : person.get("name"),
        "athlete_id" : person.get("athlete_id"),
        "access_token" : person.get("access_token"),
        "access_token_expired_at" : person.get("access_token_expired_at"),
        "refresh_token" : person.get("refresh_token"),
        "team_number" : person.get("team_number"),
        "mileage" : person.get("mileage"),
    })

#returns a list of all the names
def get_all_names():
    users = db.collection('Users').stream()
    names = []
    for user in users:
        names.append(user.to_dict()['name'])
    return names

#used to update any data. example to update refresh token to 12345, 
#field_name = 'access_token' and updated_data = '12345'
def update_data(user_name, field_name, updated_data):
    doc_ref = db.collection('Users').document(user_name)
    doc_ref.update({
        field_name : updated_data
    })

def update_multiple_datas(user_name, updated_data_obj):
    doc_ref = db.collection('Users').document(user_name)
    doc_ref.update(updated_data_obj)

#get name using athlete id, id input as string
def get_name(id):
    names = get_all_names()
    for name in names:
        doc_ref = db.collection('Users').document(name)
        person_ref = doc_ref.get()
        retrieved_id = person_ref.to_dict()['athlete_id']
        if (id == retrieved_id):
            print('found')
            return person_ref.to_dict()['name']

#get all data using name
def get_data(name):
    doc_ref = db.collection('Users').document(name)
    person_ref = doc_ref.get()
    name = person_ref.to_dict()['name']
    athlete_id = person_ref.to_dict()['athlete_id']
    access_token = person_ref.to_dict()['access_token']
    access_token_expired_at = person_ref.to_dict()['access_token_expired_at']
    refresh_token = person_ref.to_dict()['refresh_token']
    team_number = person_ref.to_dict()['team_number']
    mileage = person_ref.to_dict()['mileage']

    person = {
        "name" : name,
        "athlete_id" : athlete_id,
        "access_token" : access_token,
        "access_token_expired_at" : access_token_expired_at,
        "refresh_token" : refresh_token,
        "team_number" : team_number,
        "mileage" : mileage
    }

    return person

def get_sorted_names():
    names = get_all_names()
    unsorted_names = []
    for name in names:
        doc_ref = db.collection('Users').document(name)
        person_ref = doc_ref.get()
        mileage = person_ref.to_dict()['mileage']
        team_number = person_ref.to_dict()['team_number']
        person = {
            "name" : name,
            "team_number" : team_number,
            "mileage" : int(mileage)
        }
        unsorted_names.append(person)
    sorted_names = sorted(unsorted_names, key=lambda d: d["mileage"], reverse = True)
    print(sorted_names)
    return sorted_names

def get_all_team_number():
    names = get_all_names()
    name_list = []
    for name in names:
        doc_ref = db.collection('Users').document(name)
        person_ref = doc_ref.get()
        team_number = person_ref.to_dict()['team_number']
        person = {
            "name" : name,
            "team_number" : team_number,
        }
        name_list.append(person)
    print(name_list)
    return(name_list)
            

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
        doc_ref = db.collection('Teams').document(team)
        team_ref = doc_ref.get()
        mileage = team_ref.to_dict()['team_mileage']
        team_data = {
            "team_id" : team,
            "team_mileage" : int(mileage)
        }
        unsorted_teams.append(team_data)
    sorted_teams = sorted(unsorted_teams, key=lambda d: d["team_mileage"], reverse = True) 
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