#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import math as m 

class Senal(object):
    """docstring for Senal"""
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.interrupcion, bouncetime=20)  
        self.cuenta = 0 

    def interrupcion(self):
    	self.cuenta += 1
    	print "La cuenta va en %s " % self.cuenta


try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()        


		

