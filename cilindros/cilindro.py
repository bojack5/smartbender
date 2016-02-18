#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import math as m 

GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,True)
GPIO.setup(8,True)

for i in range(4):
    time.sleep(1)
    GPIO.setup(8,False)
    time.sleep(1)
    GPIO.setup(8,True)

    GPIO.setup(7,False)
    time.sleep(1)
    GPIO.setup(7,True)


