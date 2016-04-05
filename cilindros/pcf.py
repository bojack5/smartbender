#!/usr/bin/env python
from smbus import SMBus

class Pines(object):
    """docstring for Pines"""
    def __init__(self,address):
        self.estado = 0b11111111
        self.address = address

    def toggle(self,pin):
    	numero = 2**pin
        self.estado = self.estado^numero
        bus.write_byte(self.address , self.estado)
        return self.estado

    def reset(self):
        self.estado = self.estado|255
        bus.write_byte(address , self.estado)        