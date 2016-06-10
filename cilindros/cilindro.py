#!/usr/bin/env python
import time
import math as m 
import conf
from smbus import SMBus

class Pines(object):
    """docstring for Pines"""
    def __init__(self,address):
        conf.estado = 0b11111111
        self.address = address
        self.bus = SMBus(1)
    def cero(self,pin):
        conf.estado &=~(1<<pin)
        self.bus.write_byte(self.address , conf.estado)
        return conf.estado

    def uno(self , pin):
        conf.estado |=(1<<pin)
        self.bus.write_byte(self.address , conf.estado)
        return conf.estado
            
    def toggle(self,pin):
        numero = 2**pin
        conf.estado = conf.estado^numero
        self.bus.write_byte(self.address , conf.estado)
        return conf.estado

    def toggle2(self,pin1,pin2):
        self.toggle(pin1)
        self.toggle(pin2)   
    
    def reset(self):
        self.estado = self.estado|255
        self.bus.write_byte(address , self.estado)  

class Sencillo(object):
    """docstring for Simple"""
    def __init__(self,pin):
        self.estado = 0
        self.pin = pin
        self.pines = Pines(0x20)

    def salir(self):
        return self.pines.cero(self.pin)

    def entrar(self):
        return self.pines.uno(self.pin)        

        



class Doble(object):
    """docstring for Doble"""
    def __init__(self, pin1 , pin2):
        self.pines = Pines(0x20)
        self.estado = 0
        self.pin1 = pin1
        self.pin2 = pin2

    def salir(self):
        self.pines.cero(self.pin1)
        self.pines.uno(self.pin2)

    def entrar(self):
        self.pines.cero(self.pin2)
        self.pines.uno(self.pin1)  

    def reset(self):
        self.pines.uno(self.pin1)
        self.pines.uno(self.pin2)
              
        
		






