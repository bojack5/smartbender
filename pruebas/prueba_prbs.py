#!/usr/bin/env python
import sys
sys.path.append('..')
#import pid_velocidad
from prbs import prbs
import random
import time

DEBUG = True
FILE = True
VAL = 0
FORMATO_ENCABEZADO = "\t%s\t\t%s"
FORMATO_VALORES = "%d\t%f\t%f"

if(FILE):f = open("datos.log","w")

def main():
    contador = 0
    nombres = ('Prbs' , 'velocidad')
    #dato = int(prbs())
    header = FORMATO_ENCABEZADO%nombres
    velocidad = 48
    if(DEBUG):print header
    if(FILE):f.write(header+"\n")

    while (1):
    	#dato = prbs()
    	contador += 1
            	
    	body = FORMATO_VALORES % (contador , prbs() , velocidad)
        velocidad = random.choice([120,200,250,300,400,320,0,252,])#pid_velocidad.velocidad
    	if(DEBUG): print body
    	if(FILE): f.write(body + "\n")
    	time.sleep(1)

try:
    main()    	
finally:
    f.close()
