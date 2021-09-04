import subprocess
a1 = 'mpg123 -a hw:2,0 summer2.mp3'
proc = subprocess.run(a1, shell=True)