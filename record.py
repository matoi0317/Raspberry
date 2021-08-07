import subprocess
import time
import speech_recognition as sr
a1 = 'arecord -D plughw:0,0 -d 10 -f cd test3.wav'
proc = subprocess.run(a1, shell=True)
r = sr.Recognizer()
with sr.AudioFile("test3.wav") as source:
    audio = r.record(source)
print(r.recognize_google(audio))