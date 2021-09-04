"指定した時間に音楽を鳴らす"

import datetime
import time
import subprocess
time = 24
i = 1
a1 = 'mpg123 -a hw:2,0 summer2.mp3'
while i < 2:
    n = datetime.datetime.now()
    nm = n.minute
    if time == nm:
        proc = subprocess.run(a1, shell=True)
        print("音声を停止し、録音を開始します。")
        a1 = 'arecord -D plughw:0,0 -d 10 -f cd test3.wav'
        i += 1