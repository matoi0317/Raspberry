# coding: utf-8
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage
import sys
import speech_recognition as sr
import subprocess
import time
import datetime

a1 = 'mpg123 -a hw:0,0 food2.mp3'
a2 = 'arecord -D plughw:2,0 -d 10 -f cd food.wav'
a5 = 'mpg123 -a hw:0,0 monshin2.mp3'

mmm = int(input())
i = 1
args = sys.argv
user_id = args[1]
cred = credentials.Certificate('karute-81f3c-firebase-adminsdk-na7p6-099144bd72.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'karute-81f3c.appspot.com'})
db = firestore.client()
docs = db.collection("users").where("id","==",int(user_id)).get()
for doc in docs:
    while i < 2:
        n = datetime.datetime.now()
        nm = n.minute
        if mmm == nm:
            if doc.to_dict()["q1"] == True:
                # 問診の時間です
                proc = subprocess.run(a5, shell=True)
                # ご飯は食べましたか？
                proc = subprocess.run(a1, shell=True)
                # 録音
                proc = subprocess.run(a2, shell=True)
                time.sleep(0)
                i += 1

r = sr.Recognizer()
with sr.AudioFile("food.wav") as source:
    audio = r.record(source)
text = r.recognize_google(audio, language="ja-JP")
print(text)
