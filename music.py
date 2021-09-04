# coding: utf-8
from functions.Create_pdf import Create_pdf
import speech_recognition as sr
import datetime
import time
import subprocess
mmm = int(input())
count = 5
i = 1
a1 = 'mpg123 -a hw:2,0 food.mp3'
a2 = 'arecord -D plughw:0,0 -d 10 -f cd food.wav'
a3 = "mpg123 -a hw:2,0 wakeup.mp3"
a4 = 'arecord -D plughw:0,0 -d 10 -f cd wakeup.wav'
while i < 2:
    n = datetime.datetime.now()
    nm = n.minute
    if mmm == nm:
        #ご飯は食べましたか？
        proc = subprocess.run(a1, shell=True)
        #録音
        proc = subprocess.run(a2, shell=True)
        time.sleep(2)
        #何時に起きましたか？
        proc = subprocess.run(a3, shell=True)
        #録音
        proc = subprocess.run(a4, shell=True)
        time.sleep(2)
        i += 1

r = sr.Recognizer()
with sr.AudioFile("food.wav") as source:
    audio = r.record(source)
text = r.recognize_google(audio, language="ja-JP")
with sr.AudioFile("wakeup.wav") as source:
    audio2 = r.record(source)
text2 = r.recognize_google(audio2, language="ja-JP")
print("ご飯を食べましたか？＞＞"+text)
print("何時に起きましたか？>>"+text2)

Create_pdf(text, text2)
