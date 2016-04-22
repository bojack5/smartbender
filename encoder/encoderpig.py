#!/usr/bin/env python

import time

import pigpio # http://abyz.co.uk/rpi/pigpio/python.html

pi = pigpio.pi()
if not pi.connected:
    exit(0)

cb = pi.callback(21)

while True:
    print(cb.tally())
    cb.reset_tally()
    time.sleep(1)