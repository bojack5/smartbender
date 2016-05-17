#!/usr/bin/env python
from PID.pid import PID as PID
from  stepper.stepper import Nema42
from encoder.rotary_encoder2 import decoder as Encoder
import PID.operaciones as funciones
import conf2
import pigpio
import time

class PID_Velocidad(object):
    """Clase que ejecuta un PID de velocidad en la maquina dobladora"""
    def __init__(self , Kp , ki , kd):
        self.pid = PID(kp , ki , kd)
        self.motor = Nema42(conf2.pines['Nema42']['direccion'] , conf2.pines['Nema42']['pulso'])
        self.pi = pigpio.pi()
        self.encoder       = Encoder(self.pi,conf2.pines['encoder']['A'] ,
                                  conf2.pines['encoder']['B'] ,
                                 self.interrupcion ,)
        self.funciones_Nema42 = funciones.Nema42()
        self.tiempo_actual    = 0
        self.tiempo_pasado    = time.time()
        self.velocidad        = 0
        self.posicion         = 0
        self.direccion_motor  = 0

    def interrupcion(self , direccion):

    	self.tiempo_actual = time.time()
    	self.posicion     -= direccion
    	tiempo             = self.tiempo_actual - self.tiempo_pasado
    	self.velocidad     = 0.06283185307179587/time #linear movement of machine from each step of stepper motor
        self.tiempo_pasado = self.tiempo_actual
        error              = self.pid.update(self.velocidad)
        if self.velocidad < 0: self.direccion_motor = 1
        else : self.direccion_motor = 0
        self.motor.avance(self.funciones.ts_from_vel(self.velocidad-self.error),self.direccion_motor) # suma de error de velocidad y set point , asi como su actuacion 
    
    def SetPoint(self , setpoint):
        if self.velocidad < 0: self.direccion_motor = 1
        else : self.direccion_motor = 0
        self.pid.setPoint(setpoint)

        ts = self.funciones_Nema42.ts_from_vel(setpoint)
        self.motor.avance(ts,self.direccion_motor)

    

        		





