#!/usr/bin/env python
import pigpio

class Nema23(object):
    """docstring for Nema23"""
    def __init__(self, pin_enable , pin_direccion , pin_pulse):
        self.pin_direccion = pin_direccion
        self.pin_pulse     = pin_pulse
        self.pin_enable    = pin_enable
        self.pi = pigpio.pi()
        self.pi.set_mode(self.pin_direccion, pigpio.OUTPUT)
        self.pi.set_mode(self.pin_pulse, pigpio.OUTPUT)
        self.pi.set_mode(self.pin_enable, pigpio.OUTPUT)

    def avance(self , tus ,direccion ):
    	self.pi.wave_clear()
        self.pi.wave_add_generic([
            pigpio.pulse(0,1<<self.pin_pulse,tus),
            pigpio.pulse(1<<self.pin_pulse,0,tus),])
        wid = self.pi.wave_create()
        self.pi.write(self.pin_enable , 0)
        self.pi.wave_send_repeat(wid)

    def parar(self):
        self.pi.write(self.pin_enable , 1)
        self.pi.wave_tx_stop()    


class Nema42(object):
    """docstring for Nema42"""
    def __init__(self, pin_direccion , pin_pulse):
        self.pin_direccion = pin_direccion
        self.pin_pulse     = pin_pulse
        self.pi = pigpio.pi()
        self.pi.set_mode(self.pin_direccion, pigpio.OUTPUT)
        self.pi.set_mode(self.pin_pulse, pigpio.OUTPUT)

    def avance(self , tus , direccion):
        self.pi.write(self.pin_direccion , direccion)
        if tus > 3000: tus = 3000
        elif tus < 1000 : tus = 1000
        self.pi.wave_clear()
        self.pi.wave_add_generic([
            pigpio.pulse(0,1<<self.pin_pulse,tus),
            pigpio.pulse(1<<self.pin_pulse,0,tus),])
        wid = self.pi.wave_create()
        self.pi.wave_send_repeat(wid)

    def parar(self):
        self.pi.wave_tx_stop()
            




    







        
        

        

        
