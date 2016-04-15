#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import math as m 

GPIO.setmode(GPIO.BCM)


class Nema23(object):
    """docstring for Nema23"""
    def __init__(self, pin_enable , pin_direccion , pin_pulse):
        GPIO.setup(pin_enable,GPIO.OUT)
        GPIO.setup(pin_direccion,GPIO.OUT)
        GPIO.setup(pin_pulse,GPIO.OUT)
    	self.pin_enable    = pin_enable
    	self.pin_direccion = pin_direccion
    	self.pin_pulse     = pin_pulse

    def avance(self , direccion , pasos , velocidad):
    	GPIO.output(self.pin_enable,False)
    	GPIO.output(self.pin_direccion , direccion)
    	vel = 1./velocidad

    	for paso in xrange(0,pasos):
            GPIO.output(self.pin_pulse,False)
            time.sleep(vel)
            GPIO.output(self.pin_pulse,True)
            time.sleep(vel)

        GPIO.output(self.pin_enable,True)
        GPIO.output(self.pin_direccion,True)


class Nema42(object):
    """docstring for Nema42"""
    def __init__(self, pin_direccion , pin_pulse):
        GPIO.setup(pin_pulse,GPIO.OUT)
        GPIO.setup(pin_direccion,GPIO.OUT)
        self.pin_direccion = pin_direccion
        self.pin_pulse     = pin_pulse
		
    def avance(self , direccion , velocidad , pasos):
        GPIO.output(self.pin_direccion , direccion)
        vel = 1./velocidad

    	for paso in xrange(0,pasos):
            GPIO.output(self.pin_pulse,False)
            time.sleep(vel)
            GPIO.output(self.pin_pulse,True)
            time.sleep(vel)

        GPIO.output(self.pin_direccion,True)    





        
        

        

        
