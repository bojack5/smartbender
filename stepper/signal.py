
#!/usr/bin/python
#######
# This program would generate Squence pulse train on GPIO 7 Pin 26 of P1
#######
import RPi.GPIO as GPIO
from time import sleep
import sys
import signal

def signal_handler(signal, frame):
  print
  GPIO.cleanup()
  sys.exit(0)

def lopper():
  for i in range(400):
    GPIO.output(7,0)
    sleep(0.00025)
    GPIO.output(7,1)
    sleep(0.00025)

GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT)
signal.signal(signal.SIGINT,signal_handler)
print("Press Ctrl+c to Stop Pulse train")
lopper()
GPIO.cleanup()
