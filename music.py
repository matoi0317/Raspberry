# coding: utf-8
from functions.monshin import Create_pdf
from functions.firebase import send_pdf
import speech_recognition as sr
import datetime
import time
import subprocess
from subprocess import PIPE
from functions.serial import getserial
mmm = int(input())
count = 5
i = 1
a1 = 'mpg123 -a hw:0,0 food2.mp3'
a2 = 'arecord -D plughw:0,0 -d 10 -f cd food.wav'
a3 = "mpg123 -a hw:0,0 wakeup2.mp3"
a4 = 'arecord -D plughw:0,0 -d 10 -f cd wakeup.wav'
a5 = 'mpg123 -a hw:0,0 monshin2.mp3'
a6 = 'mpg123 -a hw:0,0 medicine2.mp3'
a7 = 'arecord -D plughw:0,0 -d 10 -f cd medicine.wav'
a8 = 'mpg123 -a hw:0,0 syoujou2.mp3'
a9 = 'arecord -D plughw:0,0 -d 10 -f cd syoujou.wav'
a10 = 'mpg123 -a hw:0,0 end.mp3'
while i < 2:
    n = datetime.datetime.now()
    nm = n.minute
    if mmm == nm:
        #問診の時間です
        proc = subprocess.run(a5, shell=True)
        #ご飯は食べましたか？
        proc = subprocess.run(a1, shell=True)
        #録音
        proc = subprocess.run(a2, shell=True)
        time.sleep(0)
        #何時に起きましたか？
        proc = subprocess.run(a3, shell=True)
        #録音
        proc = subprocess.run(a4, shell=True)
        time.sleep(0)
        #処方された薬は飲みましたか？
        proc = subprocess.run(a6, shell=True)
        #録音
        proc = subprocess.run(a7, shell=True)
        time.sleep(0)
        #体に何か症状はありますか？
        proc = subprocess.run(a8, shell=True)
        #録音
        proc = subprocess.run(a9, shell=True)
        time.sleep(0)
        #終了
        proc = subprocess.run(a10, shell=True)
        i += 1

r = sr.Recognizer()
with sr.AudioFile("food.wav") as source:
    audio = r.record(source)
text = r.recognize_google(audio, language="ja-JP")
with sr.AudioFile("wakeup.wav") as source:
    audio2 = r.record(source)
text2 = r.recognize_google(audio2, language="ja-JP")
with sr.AudioFile("medicine.wav") as source:
    audio3 = r.record(source)
text3 = r.recognize_google(audio3, language="ja-JP")
with sr.AudioFile("syoujou.wav") as source:
    audio4 = r.record(source)
text4 = r.recognize_google(audio4, language="ja-JP")
print("ご飯を食べましたか？＞＞"+text)
print("何時に起きましたか？>>"+text2)
print("処方された薬は飲みましたか？>>"+text3)
print("体に何か症状はありますか？??"+text4)

Create_pdf(text, text2, text3, text4)
myserial = getserial()
