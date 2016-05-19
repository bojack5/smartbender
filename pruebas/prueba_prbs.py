#!/usr/bin/env python
import sys
sys.path.append('..')
#from pid_velocidad import PID_Velocidad as pidv
from rotary_encoder2 import decoder
from prbs import prbs
import random
import time

DEBUG = False
FILE = True
VAL = 0
FORMATO_ENCABEZADO = "\t%s\t\t%s"
FORMATO_VALORES = "%d\t%f\t%f"

if(FILE):f = open("prbs40_3s.log","w")

def main():
    global pid
    contador = 0
    nombres = ('Prbs' , 'velocidad')
    #dato = int(prbs())
    encoder = decoder(6,13)
    header = FORMATO_ENCABEZADO%nombres
    
    if(DEBUG):print header
    if(FILE):f.write(header+"\n")

    while (contador < 10000):
    	#dato = prbs()
    	#print contador%300
        if not contador%300:
            valor_prbs = prbs()
            encoder.pid_velocidad.SetPoint(valor_prbs)
            print "Valor prbs = %s"%valor_prbs
        velocidad = encoder.velocidad
    	body = FORMATO_VALORES % (contador , valor_prbs , velocidad)
        
    	if(DEBUG): print body
    	if(FILE): f.write(body + "\n")
    	time.sleep(0.01)
        contador += 1
    encoder.cancel()
    encoder.pid_velocidad.motor.parar()
    encoder.pi.stop()    

try:
    main()    	
finally:    
    f.close()
