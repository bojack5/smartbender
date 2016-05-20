#!/usr/bin/env python
from PID.pid import PID 
from pid_velocidad import PID_Velocidad as pidv
import PID.operaciones as funciones

class PID_Posicion(object):
    """docstring for PID_Posicion"""
    def __init__(self, kp = 1.0 , ki =0.0, kd =0.0):
        self.pid  = PID(kp , ki , kd)
        self.pid_velocidad = pidv()
        #self.funciones_Nema42 = funciones.Nema42()
        #self.dist_x_pulso_encoder = 0.12566370614359174

    def SetPoint(self , setpoint):
        self.pid_posicion.pid.setPoint(abs(setpoint))	
        if setpoint > 0: direccion = -1
        elif setPoint < 0: direccion = 1
        sp = 3000 - abs(setpoint)
        if sp < 1000 : sp = 1000
        sp = sp *direccion
        self.pid_velocidad.SetPoint(sp)


            
