#!/usr/bin/env python
import pigpio

class decoder:

   """Clase para decodificar los pulsos de un encoder mecanico."""

   def __init__(self, pi, gpioA, gpioB, callback):

      self.pi = pi
      self.gpioA = gpioA
      self.gpioB = gpioB
      self.callback = callback
      self.velocidad = 0
      

      self.levA = 0
      self.levB = 0

      self.lastGpio = None

      self.pi.set_mode(gpioA, pigpio.INPUT)
      self.pi.set_mode(gpioB, pigpio.INPUT)

      self.pi.set_pull_up_down(gpioA, pigpio.PUD_UP)
      self.pi.set_pull_up_down(gpioB, pigpio.PUD_UP)

      self.cbA = self.pi.callback(gpioA, pigpio.EITHER_EDGE, self._pulse)
      self.cbB = self.pi.callback(gpioB, pigpio.EITHER_EDGE, self._pulse)

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

   import time
   import pigpio

   import rotary_encoder

   pos = 0
   actual_time = 0
   past_time = time.time()
   velocidad = 0
   def callback(way):
      
      global pos
      global past_time
      global tiempo_actual
      global velocidad
      actual_time = time.time()
      pos -= way
      time = actual_time - past_time
      velocidad = 0.06283185307179587/time #linear movement of machine from each step of stepper motor
      past_time = actual_time



      

   pi = pigpio.pi()

   decoder = rotary_encoder.decoder(pi, 21, 20, callback)
   while 1:

      time.sleep(1)
      print("pos={0} vel={1}".format(pos,velocidad))


   decoder.cancel()

   pi.stop()

