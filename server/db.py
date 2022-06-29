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
        "athlete id" : person.get("athlete id"),
        "access token" : person.get("access token"),
        "access token expired at" : person.get("access token expired at"),
        "refresh token" : person.get("refresh token"),
        "team number" : person.get("team number"),
        "mileage" : person.get("mileage"),
    })



def main():
    #test()

    #sample data
    name = "zhen hong"
    athlete_id = 179456
    access_token = 123
    access_token_expired_at = 456
    refresh_token = 999
    team_number = 2
    mileage = 50

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

    add_person(person)

if __name__ == "__main__":
    main()