
#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import math as m 

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

def avance(velocidad , pasos,direccion):
    vel = 1./velocidad
    GPIO.output(20,direccion)
    for i in range(pasos):
        GPIO.output(21,True)
        print "Paso %s\n"%(i+1)
        time.sleep(vel)
        GPIO.output(21,False)
        time.sleep(vel)
    GPIO.output(20,True)

def lineal():
    count = 0.0015
    try:
        while True:
            if count < 0.0005:
                print "limite alcanzado!"
                count = 0.0005
            GPIO.output(7,True)
            time.sleep(count)
            GPIO.output(7,False)
            time.sleep(count)
            count -= 0.000001


    except KeyboardInterrupt:
        print "Velocidad maxima = %s"%count

def uno_en_n():
    count = 240
    try:
        while True:
            GPIO.output(7,True)
            time.sleep(1.0/count)
            GPIO.output(7,False)
            time.sleep(1.0/count)
            count += 1


    except KeyboardInterrupt:
        print "Velocidad maxima = %s"%count        

def escalonada():
    count = 0.001
    try:
        while True:
            for i in range(30):
                GPIO.output(7,True)
                time.sleep(count)
                GPIO.output(7,False)
                time.sleep(count)
            count -= 0.00001


    except KeyboardInterrupt:
        print "Velocidad maxima = %s"%count
        

def rampa(pasos):
    cambio = 0.1/pasos
    
    for i in range(100):
        GPIO.output(7,True)
        time.sleep(0.1-cambio)
        print "Vuelta %s \n"%(i+1)
        GPIO.output(7,False)
        cambio += (1/10.)*cambio


#    for i in range(pasos):
#        GPIO.output(7,True)
#        if i > (3/4.)*pasos:
##            vel-=0.01
#            if vel<=0.0001:
#                vel = 0.0001
#        print "Paso %s\n"%(i+1)
#        time.sleep(vel)
#        GPIO.output(7,False)
#        time.sleep(vel)


avance(1000,2000,0)
