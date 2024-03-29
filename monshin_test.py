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
import busio
import board
import adafruit_amg88xx
import math

#ご飯
a1 = 'mpg123 -a hw:2,0 food2.mp3'
a2 = 'arecord -D plughw:0,0 -d 10 -f cd food.wav'
#起きた時間
a3 = "mpg123 -a hw:2,0 wakeup2.mp3"
a4 = 'arecord -D plughw:0,0 -d 10 -f cd wakeup.wav'
a5 = 'mpg123 -a hw:2,0 monshin2.mp3'
#薬
a6 = 'mpg123 -a hw:2,0 medicine2.mp3'
a7 = 'arecord -D plughw:0,0 -d 10 -f cd medicine.wav'
#何か症状ある?
a8 = 'mpg123 -a hw:2,0 syoujou2.mp3'
a9 = 'arecord -D plughw:0,0 -d 10 -f cd syoujou.wav'
#熱?
a10 = 'mpg123 -a hw:2,0 fever.mp3'
a11 = 'arecord -D plughw:0,0 -d 10 -f cd fever2.wav'
#喉
a12 = 'mpg123 -a hw:2,0 nodo.mp3'
a13 = 'arecord -D plughw:0,0 -d 10 -f cd nodo2.wav'
#排尿
a14 = 'mpg123 -a hw:2,0 nyo.mp3'
a15 = 'arecord -D plughw:0,0 -d 10 -f cd nyo2.wav'
#便秘
a16 = 'mpg123 -a hw:2,0 benpi.mp3'
a17 = 'arecord -D plughw:0,0 -d 10 -f cd benpi2.wav'
#お腹
a18 = 'mpg123 -a hw:2,0 onaka.mp3'
a19 = 'arecord -D plughw:0,0 -d 10 -f cd onaka2.wav'
a20 = 'mpg123 -a hw:0,0 end.mp3'

mmm = int(input())
i = 1
args = sys.argv
user_id = args[1]
cred = credentials.Certificate('karute-81f3c-firebase-adminsdk-na7p6-099144bd72.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'karute-81f3c.appspot.com'})
db = firestore.client()
docs = db.collection("users").where("id","==",int(user_id)).get()
while i < 2:
    n = datetime.datetime.now()
    nm = n.minute
    if mmm == nm:
        #問診の時間です
        proc = subprocess.run(a5, shell=True)
        for doc in docs:
            if doc.to_dict()["q1"] == True:
                proc = subprocess.run(a6, shell=True)
                proc = subprocess.run(a7, shell=True)
                time.sleep(0)
            if doc.to_dict()["q2"] == True:
                proc = subprocess.run(a1, shell=True)
                # 録音
                proc = subprocess.run(a2, shell=True)
                time.sleep(0)
            if doc.to_dict()["q3"] == True:
                proc = subprocess.run(a3, shell=True)
                # 録音
                proc = subprocess.run(a4, shell=True)
                time.sleep(0)
            if doc.to_dict()["q4"] == True:
                proc = subprocess.run(a10, shell=True)
                # 録音
                proc = subprocess.run(a11, shell=True)
                time.sleep(0)
                r = sr.Recognizer()
            if doc.to_dict()["q5"] == True:
                proc = subprocess.run(a12, shell=True)
                # 録音
                proc = subprocess.run(a13, shell=True)
                time.sleep(0)
            if doc.to_dict()["q6"] == True:
                proc = subprocess.run(a14, shell=True)
                # 録音
                proc = subprocess.run(a15, shell=True)
                time.sleep(0)
            if doc.to_dict()["q7"] == True:
                proc = subprocess.run(a16, shell=True)
                # 録音
                proc = subprocess.run(a17, shell=True)
                time.sleep(0)
            if doc.to_dict()["q8"] == True:
                proc = subprocess.run(a18, shell=True)
                # 録音
                proc = subprocess.run(a19, shell=True)
                time.sleep(0)
            if doc.to_dict()["q9"] == True:
                proc = subprocess.run(a8, shell=True)
                # 録音
                proc = subprocess.run(a9, shell=True)
                time.sleep(0)

        i += 1

# I2Cバス、センサーの初期化
i2c_bus = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x69)
total = 0
# ちょっと待つ
time.sleep(.1)

# ループ開始
for k in range(1):
    # データ取得
    sensordata = sensor.pixels
    # for i in sensordata:
    #     print(max(i))
for i in sensordata:
    for j in i:
        total += j
print(math.floor(total/64)-15)
tempureture = math.floor(total/64)-15



r = sr.Recognizer()
if doc.to_dict()["q1"] == True:
    print("madi-------")
    with sr.AudioFile("medicine.wav") as source:
        print("medi--with-----")
        audio3 = r.record(source)
        print("audio----medi---")
    text3 = r.recognize_google(audio3, language="ja-JP")
    print(text3)
else:
    text3 = ""
if doc.to_dict()["q2"] == True:
    print("food-----")
    with sr.AudioFile("food.wav") as source:
        print("with-----")
        audio = r.record(source)
    text = r.recognize_google(audio, language="ja-JP")
    print(text)
else:
    text = ""
if doc.to_dict()["q3"] == True:
    with sr.AudioFile("wakeup.wav") as source:
        audio2 = r.record(source)
    text2 = r.recognize_google(audio2, language="ja-JP")
    print(text2)
else:
    text2 = ""
if doc.to_dict()["q9"] == True:
    with sr.AudioFile("syoujou.wav") as source:
        audio4 = r.record(source)
    text4 = r.recognize_google(audio4, language="ja-JP")
else:
    text4 = ""
if doc.to_dict()["q4"] == True:
    with sr.AudioFile("fever2.wav") as source:
        audio5 = r.record(source)
    text5 = r.recognize_google(audio5, language="ja-JP")
else:
    text5 = ""
if doc.to_dict()["q5"] == True:
    with sr.AudioFile("nodo2.wav") as source:
        audio6 = r.record(source)
    text6 = r.recognize_google(audio6, language="ja-JP")
else:
    text6 = ""
if doc.to_dict()["q6"] == True:
    with sr.AudioFile("nyo2.wav") as source:
        audio7 = r.record(source)
    text7 = r.recognize_google(audio7, language="ja-JP")
else:
    text7 = ""
if doc.to_dict()["q7"] == True:
    with sr.AudioFile("benpi2.wav") as source:
        audio8 = r.record(source)
    text8 = r.recognize_google(audio8, language="ja-JP")
else:
    text8 = ""
if doc.to_dict()["q8"] == True:
    print("onaka--------")
    with sr.AudioFile("onaka2.wav") as source:
        audio9 = r.record(source)
        print("audio999999")
    text9 = r.recognize_google(audio9, language="ja-JP")
    print(text9)
else:
    text9 = ""

Create_pdf(text, text2,text3,text4,text5,text6,text7,text8,text9,int(user_id),tempureture)

