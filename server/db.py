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

def add_person(person):
    doc_ref = db.collection('Users').document(person.get("name"))
    doc_ref.set({
        "name" : person.get("name"),
        "athlete id" : person.get("athlete id"),
        "access token" : person.get("access token"),
        "access token expired at" : person.get("access token expired at"),
        "refresh token" : person.get("refresh token"),
        "team number" : person.get("team number"),
        "mileage" : person.get("mileage"),
    })

def get_all_names():
    users = db.collection('Users').stream()
    names = []
    for user in users:
        names.append(user.to_dict()['name'])
    print(names)
    return names


def update_mileage(name, num):
    doc_ref = db.collection('Users').document(name)
    doc_ref.update({
        "mileage" : num
    })



def main():
    #test()

    #sample data
    name = "wen feng"
    athlete_id = '179456'
    access_token = '123@123'
    access_token_expired_at = '456@456'
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
    #update_mileage("zhen hong", 100)
    get_all_names()

if __name__ == "__main__":
    main()