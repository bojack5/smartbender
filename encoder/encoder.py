#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import math as m 

class Senal(object):
    """docstring for Senal"""
    def __init__(self, pinA , pinB):
        self.pinA = pinA
        self.pinB = pinB
        self.estado = 0
        GPIO.setup(self.pinA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pinB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.interrupcionA, bouncetime=1)  
        GPIO.add_event_detect(self.pin, GPIO.BOTH, callback=self.interrupcionB, bouncetime=1)
        self.cuenta = 0 

    def interrupcionA(self , pin):
    	if self.estado:
    	    self.cuenta += 1

    	if not self.estado:
    	    self.cuenta -= 1

    	print "La cuenta va en %s " % self.cuenta

    def interrupcionB(self , pin):
        if GPIO.input(self.pin):
            self.estado = 1
        if GPIO.input(self.pin) == 0:
            self.estado = 0    	
        print "Estado = %s" % self.estado



        
    

		
try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()        


		

