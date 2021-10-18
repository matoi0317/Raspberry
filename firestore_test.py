import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage
import datetime

dt_now = datetime.datetime.now()
datetime_format = dt_now.strftime("%Y%m%d%H%M%S")
datetime_web = dt_now.strftime("%Y年%m月%d日%H時%M分")
print(datetime_format)

cred = credentials.Certificate('karute-81f3c-firebase-adminsdk-na7p6-099144bd72.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'karute-81f3c.appspot.com'})

db = firestore.client()
docs = db.collection("items").document(datetime_format).set({
    "pdf": "https://firebasestorage.googleapis.com/v0/b/karute-81f3c.appspot.com/o/b.pdf?alt=media&token=ec8a5891-fbab-4d04-89df-9981e9b0aa9f",
    "date":datetime_web
})
