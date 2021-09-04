"指定した時間に音楽を鳴らす→録音"
import speech_recognition as sr
import datetime
import time
import subprocess
mmm = int(input())
count = 5
i = 1
a1 = 'mpg123 -a hw:2,0 free.mp3'
a2 = 'arecord -D plughw:0,0 -d 10 -f cd test3.wav'
while i < 2:
    n = datetime.datetime.now()
    nm = n.minute
    if mmm == nm:
        proc = subprocess.run(a1, shell=True)
        print("音声を停止し、録音を開始します。")
        proc = subprocess.run(a2, shell=True)
        time.sleep(3)
        i += 1

r = sr.Recognizer()
with sr.AudioFile("test3.wav") as source:
    audio = r.record(source)
text = r.recognize_google(audio, language="ja-JP")
print(text)
