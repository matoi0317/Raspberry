import subprocess
import speech_recognition as sr

a1 = 'arecord -D plughw:1,0 -d 10 test3.wav'
proc = subprocess.Popen(a1, shell=True)
proc.wait(11)
r = sr.Recognizer()
with sr.AudioFile("test3.wav") as source:
    audio = r.record(source)
print("You said: \n[" + r.recognize_google(audio) + "]")