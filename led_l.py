# coding:utf-8
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # GPIO番号で指定
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.LOW)