# coding: utf-8
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage
import datetime

def send_store(url, user_id):
    dt_now = datetime.datetime.now()
    datetime_format = dt_now.strftime("%Y%m%d%H%M%S")
    datetime_web = dt_now.strftime("%Y年%m月%d日%H時%M分")
    db = firestore.client()
    docs = db.collection("items").document(datetime_format).set({
        "pdf": url,
        "date":datetime_web,
        "user_id":user_id
    })
