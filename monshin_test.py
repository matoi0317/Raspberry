# coding: utf-8
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage
db = firestore.client()
docs = db.collection("users").get()
for doc in docs:
    print(doc.to_dict())
# # coding: utf-8
# from functions.monshin import Create_pdf
# from functions.firebase import send_pdf
# import speech_recognition as sr
# import datetime
# import time
# import subprocess
# from subprocess import PIPE
# from functions.serial import getserial
# import sys
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore, storage
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore, storage
# mmm = int(input())
# count = 5
# i = 1
# a1 = 'mpg123 -a hw:0,0 food2.mp3'
# a2 = 'arecord -D plughw:0,0 -d 10 -f cd food.wav'
# a3 = "mpg123 -a hw:0,0 wakeup2.mp3"
# a4 = 'arecord -D plughw:0,0 -d 10 -f cd wakeup.wav'
# a5 = 'mpg123 -a hw:0,0 monshin2.mp3'
# a6 = 'mpg123 -a hw:0,0 medicine2.mp3'
# a7 = 'arecord -D plughw:0,0 -d 10 -f cd medicine.wav'
# a8 = 'mpg123 -a hw:0,0 syoujou2.mp3'
# a9 = 'arecord -D plughw:0,0 -d 10 -f cd syoujou.wav'
# a10 = 'mpg123 -a hw:0,0 end.mp3'
# while i < 2:
#     n = datetime.datetime.now()
#     nm = n.minute
#     if mmm == nm:
#         #ご飯は食べましたか？
#         proc = subprocess.run(a1, shell=True)
#         #録音
#         proc = subprocess.run(a2, shell=True)
#         time.sleep(0)
#         #何時に起きましたか？
#         proc = subprocess.run(a3, shell=True)
#         #録音
#         proc = subprocess.run(a4, shell=True)
#         time.sleep(0)
#         #処方された薬は飲みましたか？
#         proc = subprocess.run(a6, shell=True)
#         #録音
#         proc = subprocess.run(a7, shell=True)
#         time.sleep(0)
#         #体に何か症状はありますか？
#         proc = subprocess.run(a8, shell=True)
#         #録音
#         proc = subprocess.run(a9, shell=True)
#         time.sleep(0)
#         #終了
#         proc = subprocess.run(a10, shell=True)
#         i += 1
#
# r = sr.Recognizer()
# with sr.AudioFile("food.wav") as source:
#     audio = r.record(source)
# text = r.recognize_google(audio, language="ja-JP")
# print(text)