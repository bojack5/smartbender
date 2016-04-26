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

    def ts_2_freq(self , ts ):
        #GPIO.output(self.pin_direccion , direccion)
        print("Funcionando con Ts={}".format(ts))
        for i in xrange(0,100):

            GPIO.output(self.pin_pulse,False)
            time.sleep(ts)
            GPIO.output(self.pin_pulse,True)
            time.sleep(ts)
            

            
		
    def avance(self , direccion , velocidad , pasos):
        GPIO.output(self.pin_direccion , direccion)
        vel = 1./velocidad

    	for paso in xrange(0,pasos):
            GPIO.output(self.pin_pulse,False)
            time.sleep(vel)
            GPIO.output(self.pin_pulse,True)
            time.sleep(vel)

        GPIO.output(self.pin_direccion,True)

    def vel2pulsos(self , velocidad , distancia):
    	perimetro = 125.66370614359172 #mm
    	pulsos = velocidad * 2000 / perimetro
    	slp = 1./(2*pulsos)
    	pasos = (distancia/perimetro)*2000
    	print "Funcionando a una velocidad de %s mm/s \t a %s pulsos cada segundo."
    	cuenta = 0
    	try:
            for i in xrange(0,pasos):
                GPIO.output(self.pin_pulse,False)
                cuenta += 1
                time.sleep(slp)
                GPIO.output(self.pin_pulse,True)
                time.sleep(slp)
            print "Se dieron %s pasos , deberian de ser %s " % (cuenta , pasos)    



    	except KeyboardInterrupt:
            print "Terminado de girar"
            GPIO.cleanup()


if __name__ == '__main__':
    traccion = Nema42(19,26)
    for i in xrange(1,1000000):
        traccion.ts_2_freq(i/1000000.)







        
        

        

        
