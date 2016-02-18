#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import math as m 

GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)

def avance(velocidad , pasos,direccion):
    vel = 1./velocidad
    GPIO.output(8,direccion)
    for i in range(pasos):
        GPIO.output(7,True)
        #print "Paso %s\n"%(i+1)
        time.sleep(vel)
        GPIO.output(7,False)
        time.sleep(vel)
    GPIO.output(8,True)

def rampa(pasos):
    cambio = 0.1/pasos
    
    for i in range(100):
        GPIO.output(7,True)
        time.sleep(0.1-cambio)
        print "Vuelta %s \n"%(i+1)
        GPIO.output(7,False)
        cambio += (1/10.)*cambio


#    for i in range(pasos):
#        GPIO.output(7,True)
#        if i > (3/4.)*pasos:
##            vel-=0.01
#            if vel<=0.0001:
#                vel = 0.0001
#        print "Paso %s\n"%(i+1)
#        time.sleep(vel)
#        GPIO.output(7,False)
#        time.sleep(vel)


#avance(4000,400,1)
