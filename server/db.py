import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from grpc import access_token_call_credentials

cred = credentials.Certificate('./server/ServiceAccountKey.json')
firebase_admin.initialize_app(cred)
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
        "athlete_id" : person.get("athlete id"),
        "access_token" : person.get("access token"),
        "access_token_expired_at" : person.get("access token expired at"),
        "refresh_token" : person.get("refresh token"),
        "team_number" : person.get("team number"),
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
        "athlete id" : athlete_id,
        "access token" : access_token,
        "access token expired at" : access_token_expired_at,
        "refresh token" : refresh_token,
        "team number" : team_number,
        "mileage" : mileage
    }

    return person


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
        "athlete id" : athlete_id,
        "access token" : access_token,
        "access token expired at" : access_token_expired_at,
        "refresh token" : refresh_token,
        "team number" : team_number,
        "mileage" : mileage
    }

    #add_person(person)
    #update_mileage("wen feng", 1200)
    #get_all_names()
    #update_data("zhen hong", "athlete_id", "789123")
    #get_name('987654')
    get_data("jason")


if __name__ == "__main__":
    main()