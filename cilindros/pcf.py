#!/usr/bin/env python
from smbus import SMBus
import conf
class Pines(object):
    """docstring for Pines"""
    def __init__(self,address):
        self.estado = 0b11111111
        self.address = address
        self.bus = SMBus(1)

    def toggle(self,pin):
    	numero = 2**pin
        self.estado = self.estado^numero
        self.bus.write_byte(self.address , self.estado)
        return self.estado
    def toggle2(self,pin1,pin2):
        self.toggle(pin1)
        self.toggle(pin2)   
    

    def reset(self):
        self.estado = self.estado|255
        self.bus.write_byte(self.address , self.estado)        
