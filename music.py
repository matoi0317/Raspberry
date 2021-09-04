import datetime
import time
import subprocess
time = "15"
a1 = 'mpg123 -a hw:2,0 summer2.mp3'
n = datetime.datetime.now()
nm = n.minute
if time == nm:
    proc = subprocess.run(a1, shell=True)