#!/usr/bin/env python2
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def A(channel):
    print "Interrupcion detectada en A"

def B(channel):
    print "falling edge detected on 23"

GPIO.add_event_detect(6, GPIO.RISING, callback=A, bouncetime=1)

#GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback2, bouncetime=300)

try:
    while 1:
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit

