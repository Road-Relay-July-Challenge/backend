import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./ServiceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

#testing stuff
user_id = 'zhenhong'
doc_ref = db.collection('Users').document(user_id)
doc_ref.set({
    'Name':'zhen hong'
})