#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

class PWM(object):
	"""docstring for PWM"""
	def __init__(self, pin , frecuencia = 150):
		self.pin = pin
		self.frecuencia = frecuencia
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin, GPIO.OUT)
		self.pin = pin
		self.pwm = GPIO.PWM(self.pin, self.frecuencia)


	def start(self):
		self.pwm.start(0)

	def set_duty(self,dc):
		self.pwm.ChangeDutyCycle(dc)

	def stop(self):
		self.pwm.stop()

if __name__ == '__main__':
	pwm = PWM(7)
	pwm.start()
        while True:

       	    for dc in range(1,100,1):
	        pwm.set_duty(dc)
		a = raw_input('Presiona enter para continuar :')
		print dc
	        time.sleep(0.02)

	    for dc in range(1,100,1):
                pwm.set_duty(100-dc)
		print dc
                time.sleep(0.02)

	pwm.stop()
