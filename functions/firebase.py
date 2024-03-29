import pyrebase
from functions.firestore_test import send_store
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage

def send_pdf(pdf, user_id,tempureture):
    config = {
        "apiKey": "AIzaSyDPeg9J4uFdpXRPeX9LsWibXVda4lstWQk",
        "authDomain": "karute-81f3c.firebaseapp.com",
        "databaseURL": "https://karute-81f3c-default-rtdb.firebaseio.com",
        "projectId": "karute-81f3c",
        "storageBucket": "karute-81f3c.appspot.com",
        "messagingSenderId": "369985687952",
        "appId": "1:369985687952:web:c94ff519f492f40436a315",
        "measurementId": "G-3ND3M4QHY7"
    }
    firebase_storage = pyrebase.initialize_app(config)
    #storage = firebase_storage.storage()
    #storage.child(pdf).put(pdf)
    blob = storage.bucket("karute-81f3c.appspot.com").blob(pdf)
    aaa = blob.upload_from_filename(pdf)
    print("AAA:", aaa)
    # url = storage.child(pdf).get_url(token=None)
    url = "https://firebasestorage.googleapis.com/v0/b/karute-81f3c.appspot.com/o/"+pdf+"?alt=media"
    send_store(url, user_id,tempureture)