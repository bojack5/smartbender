#!/usr/bin/env python

# ramp_frequency.py
# 2016-01-21
# Public Domain

import time
import pigpio

def generate_ramp(GPIO, ramp):
   l = len(ramp)
   wid=[-1] * l
   pi.set_mode(GPIO, pigpio.OUTPUT)

   # generate a wave per frequency

   for i in range(l):
      f = ramp[i][0]
      micros = int(500000/f)
      wf=[]
      wf.append(pigpio.pulse(1<<GPIO, 0,       micros))
      wf.append(pigpio.pulse(0,       1<<GPIO, micros))
      pi.wave_add_generic(wf)
      wid[i] = pi.wave_create()

   # generate a chain of waves

   chain = []

   for i in range(l):
      steps = ramp[i][1]
      x = steps & 255
      y = steps >> 8
      chain += [255, 0, wid[i], 255, 1, x, y]

   print(chain)

   pi.wave_chain(chain) # Transmit chain.

   while pi.wave_tx_busy(): # While transmitting.
      time.sleep(0.1)

   # delete all waves
   for i in range(l):
      pi.wave_delete(wid[i])

pi = pigpio.pi()

if not pi.connected:
   exit(0)

generate_ramp(7, [[2000, 100], [3000, 200], [3000, 4000]])

pi.stop()
