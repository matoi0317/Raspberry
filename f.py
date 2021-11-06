# coding: utf-8
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage
import datetime

dt_now = datetime.datetime.now()
datetime_format = dt_now.strftime("%Y%m%d%H%M%S")
datetime_web = dt_now.strftime("%Y年%m月%d日%H時%M分")

cred = credentials.Certificate('karute-81f3c-firebase-adminsdk-na7p6-099144bd72.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'karute-81f3c.appspot.com'})

db = firestore.client()
docs = db.collection("items").document(datetime_format).set({
    "pdf": "https://firebasestorage.googleapis.com/v0/b/karute-81f3c.appspot.com/o/sample.pdf?alt=media&token=9c98b48b-63a5-400c-afbf-593420cc52d3",
    "date":datetime_web
})
