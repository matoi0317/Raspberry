# coding: utf-8
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage
import sys
import speech_recognition as sr
import subprocess
import time
import datetime
from functions.monshin import Create_pdf

#ご飯
a1 = 'mpg123 -a hw:2,0 food2.mp3'
a2 = 'arecord -D plughw:0,0 -d 10 -f cd food.wav'
#起きた時間
a3 = "mpg123 -a hw:2,0 wakeup2.mp3"
a4 = 'arecord -D plughw:0,0 -d 10 -f cd wakeup.wav'
a5 = 'mpg123 -a hw:2,0 monshin2.mp3'
a6 = 'mpg123 -a hw:2,0 medicine2.mp3'
a7 = 'arecord -D plughw:0,0 -d 10 -f cd medicine.wav'
a8 = 'mpg123 -a hw:2,0 syoujou2.mp3'
a9 = 'arecord -D plughw:0,0 -d 10 -f cd syoujou.wav'
a10 = 'mpg123 -a hw:0,0 end.mp3'

mmm = int(input())
i = 1
args = sys.argv
user_id = args[1]
cred = credentials.Certificate('karute-81f3c-firebase-adminsdk-na7p6-099144bd72.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'karute-81f3c.appspot.com'})
db = firestore.client()
docs = db.collection("users").where("id","==",int(user_id)).get()
# while i < 2:
#     n = datetime.datetime.now()
#     nm = n.minute
#     if mmm == nm:
#         #問診の時間です
#         proc = subprocess.run(a5, shell=True)
#         for doc in docs:
#             if doc.to_dict()["q1"] == True:
#                 proc = subprocess.run(a1, shell=True)
#                 proc = subprocess.run(a2, shell=True)
#                 time.sleep(0)
#             else:
#                 print("False")
#             if doc.to_dict()["q2"] == True:
#                 proc = subprocess.run(a3, shell=True)
#                 # 録音
#                 proc = subprocess.run(a4, shell=True)
#                 time.sleep(0)
#             else:
#                 print("false")
#             if doc.to_dict()["q3"] == True:
#                 proc = subprocess.run(a6, shell=True)
#                 # 録音
#                 proc = subprocess.run(a7, shell=True)
#                 time.sleep(0)
#             else:
#                 print("false")
#             if doc.to_dict()["q4"] == True:
#                 proc = subprocess.run(a8, shell=True)
#                 # 録音
#                 proc = subprocess.run(a9, shell=True)
#                 time.sleep(0)
#             else:
#                 print("false")
#         i += 1
#
#
#
# r = sr.Recognizer()
# with sr.AudioFile("food.wav") as source:
#     audio = r.record(source)
# text = r.recognize_google(audio, language="ja-JP")
# print(text)
# with sr.AudioFile("wakeup.wav") as source:
#     audio2 = r.record(source)
# text2 = r.recognize_google(audio2, language="ja-JP")
# print(text2)
# with sr.AudioFile("medicine.wav") as source:
#     audio3 = r.record(source)
# text3 = r.recognize_google(audio3, language="ja-JP")
# with sr.AudioFile("syoujou.wav") as source:
#     audio4 = r.record(source)
# text4 = r.recognize_google(audio4, language="ja-JP")
text = "はい"
text2 = "いいえ"
text3 = "ok"
text4 = "no"
Create_pdf(text, text2,text3,text4,int(user_id))

