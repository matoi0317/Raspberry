# coding:utf-8
import time, subprocess, os
time_left = 20
while time_left > 0:
    print("残り時間：" + str(time_left))
    time_left -= 1
    time.sleep(1)
subprocess.Popen(['open','Desktop/sample.m4a'])