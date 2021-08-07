import subprocess
import speech_recognition as sr
for i in range(1):
    a1 = 'arecord -D plughw:0,0 -d 10 -f cd test3.wav'
    proc = subprocess.Popen(a1, shell=True)

r = sr.Recognizer()
with sr.AudioFile("test3.wav") as source:
    audio = r.record(source)
text = r.recognize_google(audio, language="ja-JP")
print(text)