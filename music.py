import datetime
import time
import subprocess
time = 19
i = 1
a1 = 'mpg123 -a hw:2,0 summer2.mp3'
while i < 2:
    n = datetime.datetime.now()
    nm = n.minute
    if time == nm:
        proc = subprocess.run(a1, shell=True)
        i += 1