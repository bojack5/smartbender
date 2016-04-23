#!/usr/bin/env python

import time
import math as m 
import pigpio # http://abyz.co.uk/rpi/pigpio/python.html


class Signal(object):
    """docstring for Interrupt"""
    def __init__(self, pinA , pinB):
        self.pinA      = pinA
        self.pinB      = pinB
        self.gpio      = pigpio.pi()
        self.perimetro = 40*m.pi
        self.cuenta    = 0
        self.estado    = 0
        self.tiempo_actual = 0 
        self.tiempo_anterior = time.time()
        self.velocidad = 0

        #Definicion de funciones que correran al interrumpirse en los pines
        self.interrupcionA  = self.gpio.callback(self.pinA, edge = pigpio.FALLING_EDGE ,func = self.guia)
        self.interrupcionB = self.gpio.callback(self.pinB, edge = pigpio.EITHER_EDGE , func = self.referencia)
        

    def guia(self,a,b,c):
        self.tiempo_actual = time.time()
        if self.estado:
        	self.cuenta += 1

        if not self.estado:
            self.cuenta -= 1

        tiempo = self.tiempo_actual-self.tiempo_anterior
        self.tiempo_anterior  = self.tiempo_actual
        self.velocidad = (self.perimetro/1000)/tiempo    

    def referencia(self,a,b,c):
        if int(self.gpio.read(self.pinB)):
            self.estado = 1
        
        if not int(self.gpio.read(self.pinB)):
            self.estado = 0                         
		
def main():
    
    encoder = Signal(21,20)
    try:
    	while 1:
            time.sleep(1)		
    except KeyboardInterrupt:
        pi.clear_bank_1(bin(2**20+2**21))

if __name__ == '__main__':
    main()        