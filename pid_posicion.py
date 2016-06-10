#!/usr/bin/env python
from PID.pid import PID 
#from pid_velocidad import PID_Velocidad as pidv
#import PID.operaciones as funciones
from stepper.stepper import Nema42

class PID_Posicion(object):
    """docstring for PID_Posicion"""
    def __init__(self, kp = 50.0 , ki =0.001, kd =0.0):
        self.pid  = PID(kp , ki , kd)
        #self.pid_velocidad = pidv()
        self.motor = Nema42(12,7)

    def SetPoint(self , setpoint):
        self.pid.setPoint(setpoint)	
        if setpoint > 0: direccion = 1
        elif setpoint <= 0: direccion = -1
        
        sp = 3000 - abs(setpoint)
        if sp < 1000 : sp = 1000
        sp = sp *direccion
        self.motor.avance(sp)


            
