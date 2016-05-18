#!/usr/bin/env python
import time
import pigpio
import numpy as np

class decoder:

   """Class to decode mechanical rotary encoder pulses."""

   def __init__(self, pi, gpioA, gpioB,):


      self.pi = pi
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
      self.archivo = open('datos_10mm_0.125_0_0.txt','w')

      

   def callback(self,way):

      self.tiempo_actual = time.time()
      self.pos += way
      tiempo = self.tiempo_actual - self.tiempo_pasado
      self.velocidad = 0.12566370614359174/tiempo#np.append(self.velocidad , 0.12566370614359174/tiempo)
      #self.velocidad.delete(0)
      self.tiempo_pasado = self.tiempo_actual
      #self.archivo.write(velocidad)

      print("posicion={}\tvelocidad={}".format(self.pos,self.velocidad))

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

   import pigpio

   import rotary_encoder2

   pos = 0

   def callback(way):

      global pos

      pos += way

      print("pos={}".format(pos))

   pi = pigpio.pi()

   decoder = rotary_encoder2.decoder(pi, 6, 13,)

   time.sleep(300)

   decoder.cancel()

   pi.stop()

