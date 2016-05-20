#!/usr/bin/env python
import time
import pigpio
from pid_posicion import PID_Posicion as pidp
#import numpy as np

class decoder:

   """Class to decode mechanical rotary encoder pulses."""

   def __init__(self, gpioA, gpioB,):


      self.pi = pigpio.pi()
      self.gpioA = gpioA
      self.gpioB = gpioB
      #self.callback = callback
      
      self.levA = 0
      self.levB = 0

      self.lastGpio = None

      self.pi.set_mode(gpioA, pigpio.INPUT)
      self.pi.set_mode(gpioB, pigpio.INPUT)

      self.pi.set_pull_up_down(gpioA, pigpio.PUD_UP)
      self.pi.set_pull_up_down(gpioB, pigpio.PUD_UP)

      self.cbA = self.pi.callback(gpioA, pigpio.EITHER_EDGE, self._pulse)
      self.cbB = self.pi.callback(gpioB, pigpio.EITHER_EDGE, self._pulse)
      """VARIABLES DE INTERRUPCION"""
      self.pos = 0
      self.tiempo_pasado = time.time()
      self.tiempo_actual = 0	
      self.velocidad = 0
      self.pid_posicion = pidp()


      #self.archivo = open('datos_10mm_0.125_0_0.txt','w')

      

   def callback(self,way):
      #print "callback"
      self.tiempo_actual = time.time()
      self.pos += way*0.12566370614359174
      tiempo = self.tiempo_actual - self.tiempo_pasado
      self.velocidad = (0.12566370614359174/tiempo)*way#np.append(self.velocidad , 0.12566370614359174/tiempo)
      self.pid_posicion.pid_velocidad.pid.update(self.velocidad)
      error = self.pid_posicion.pid.update(self.pos)
      if abs(self.pos - self.pid_posicion.pid.set_point) > 0.15:

         if error > 0 : direccion = -1
         elif error < 0 : direccion = 1
      
         sp = 3000 - abs(error)
         sp = sp * direccion
         self.pid_velocidad.SetPoint(sp) 
          
      else: 
         self.pid_posicion.pid_velocidad.SetPoint(0)
      self.tiempo_pasado = self.tiempo_actual
      print 'posicion = %s'%self.pos

   def _pulse(self, gpio, level, tick):

      """
      Decode the rotary encoder pulse.

                   +---------+         +---------+      0
                   |         |         |         |
         A         |         |         |         |
                   |         |         |         |
         +---------+         +---------+         +----- 1

             +---------+         +---------+            0
             |         |         |         |
         B   |         |         |         |
             |         |         |         |
         ----+         +---------+         +---------+  1
      """

      if gpio == self.gpioA:
         self.levA = level
      else:
         self.levB = level;

      if gpio != self.lastGpio: # debounce
         self.lastGpio = gpio

         if   gpio == self.gpioA and level == 1:
            if self.levB == 1:
               self.callback(1)
         elif gpio == self.gpioB and level == 1:
            if self.levA == 1:
               self.callback(-1)

   def cancel(self):

      """
      Cancel the rotary encoder decoder.
      """

      self.cbA.cancel()
      self.cbB.cancel()

if __name__ == "__main__":

   
   import rotary_encoder2
   
   
   decoder = rotary_encoder2.decoder( 6, 13,)
   print "kp = %s ki = %s kd = %s"%(decoder.pid_velocidad.pid.Kp ,
                                    decoder.pid_velocidad.pid.Ki , 
                                    decoder.pid_velocidad.pid.Kd)
   decoder.pid_velocidad.SetPoint(20)
   time.sleep(3)
   decoder.pid_velocidad.motor.parar()

   decoder.cancel()

   decoder.pi.stop()

