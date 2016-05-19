#!/usr/bin/env python
from PID.pid import PID 
from pid_velocidad import PID_Velocidad as pidv
import PID.operaciones as funciones

class PID_Posicion(object):
    """docstring for PID_Posicion"""
    def __init__(self, kp , ki , kd):
        self.pid_posicion  = PID(kp , ki , kd)
        self.pid_velocidad = pidv()
        self.funciones_Nema42 = funciones.Nema42()
        self.dist_x_pulso_encoder = 0.12566370614359174

    def SetPoint(self , setpoint):
    	if setpoint < 0: self.direccion_velocidad  = -1
        else : self.direccion_velocidad = 1
        self.pid_posicion.setPoint(abs(setpoint))	
            
