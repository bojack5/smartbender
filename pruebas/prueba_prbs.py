#!/usr/bin/env python
import sys
sys.path.append('..')
from pid_velocidad import PID_Velocidad as pidv
from prbs import prbs
import random
import time

DEBUG = False
FILE = True
VAL = 0
FORMATO_ENCABEZADO = "\t%s\t\t%s"
FORMATO_VALORES = "%d\t%f\t%f"

if(FILE):f = open("datos_prbs.log","w")

def main():
    global pid
    contador = 0
    nombres = ('Prbs' , 'velocidad')
    #dato = int(prbs())
    pid = pidv()
    header = FORMATO_ENCABEZADO%nombres
    
    if(DEBUG):print header
    if(FILE):f.write(header+"\n")

    while (1):
    	#dato = prbs()
    	print contador%3
        if not contador%3:
            valor_prbs = prbs()
            pid.SetPoint(valor_prbs)
            print "Valor prbs = %s"%valor_prbs
        velocidad = pid.encoder.velocidad
    	body = FORMATO_VALORES % (contador , valor_prbs , velocidad)
        
    	if(DEBUG): print body
    	if(FILE): f.write(body + "\n")
    	time.sleep(0.01)
        contador += 0.01

try:
    main()    	
finally:
    global pid
    pid.motor.parar()
    f.close()
