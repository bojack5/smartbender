#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import math as m 

class Senal(object):
    """docstring for Senal"""
    def __init__(self, pinA , pinB):
        self.pinA = pinA
        self.pinB = pinB
        self.tiempo_actual = 0 
        self.tiempo_anterior = time.time()
        self.estado = 0
        self.perimetro = 40*m.pi
        GPIO.setup(self.pinA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pinB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.interrupcionA, bouncetime=1)  
        GPIO.add_event_detect(self.pin, GPIO.BOTH, callback=self.interrupcionB, bouncetime=1)
        self.cuenta = 0 

    def interrupcionA(self , pin):
        self.tiempo_actual = time.time()
    	if self.estado:
    	    self.cuenta += 1

    	if not self.estado:
    	    self.cuenta -= 1
    	tiempo = self.tiempo_actual-self.tiempo_anterior
    	self.tiempo_anterior  = self.tiempo_actual
    	self.velocidad = (self.perimetro/1000)/tiempo   

    	#print "La cuenta va en {cuenta} y la velocidad es {velocidad}".format(cuenta = self.cuenta , velocidad = self.velocidad)

    def interrupcionB(self , pin):
        if GPIO.input(self.pin):
            self.estado = 1
        if GPIO.input(self.pin) == 0:
            self.estado = 0    	
        print "Estado = %s" % self.estado

def main():
	encoder = Senal(21,20)
	try:
	    while True:
	        time.sleep(1)
	        print "La cuenta va en {cuenta} y la velocidad es {velocidad}".format(cuenta = encoder.cuenta , velocidad = encoder.velocidad)


	except KeyboardInterrupt:
	    GPIO.cleanup()

        
    
if __name__ == '__main__':
    main()
		
        


		

