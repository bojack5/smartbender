#!/usr/bin/env python
import time
import sys
import rotary_encoder2
import math as m
from cilindros.cilindro import Sencillo , Doble

largo_prensa = 145
dm1 = 1320 
dm2 = 2250
dpr = 3820
dcz = 6700

decoder = rotary_encoder2.decoder( 6, 13,)

tr = Doble(0,1)
m1 = Sencillo(2)
m2 = Sencillo(3)
pr = Sencillo(4)
cz = Sencillo(5)
db = Doble(6,7)

prensa = []
matriz_prensa = []
magnitudes = sys.argv
magnitud_vieja = 0
contador_prensa = 0

contador = 0
for magnitud in magnitudes[1:]:
    #print "Magnitud = %s"%magnitud 
    if not magnitud_vieja: 
        magnitud_vieja = magnitud
    else :
        valor = float(float(magnitud[:-2])-float(magnitud_vieja[:-2]))
        contador += int(round(valor))
        prensa.append(contador)
        magnitud_vieja = magnitud
        #print "Magnitud_vieja = %s"%magnitud_vieja 
        
print "Prensa %s"%prensa

for i in range(len(prensa)):
    #print '...'
    if not i : pass
    else:
        contador_prensa += prensa[i-1]
        if contador_prensa+prensa[i] > 145:
            matriz_prensa.append('%s.4'%int(round((contador_prensa/0.12566370614359174)+dpr)))
            contador_prensa = 0
        if i == (len(prensa)-1): #Si es el ultimo
            #print "entrada en ultimo"
            matriz_prensa.append('%s.4'%int(round((contador_prensa+prensa[-1])/0.12566370614359174)+dpr))
    #print "Actual=%s\tUltimo=%s\t"%(i,len(prensa)-1)        

print matriz_prensa
#    if not i:
#        pass
#    else:
#        prensa.append(int(magnitudes[i])-int(magnitudes[i-1]))

#print "Prensa \n\n %s\n\n%s"%(prensa,matriz_prensa)
print "MAGNITUDES %s"%magnitudes
matriz = []

for magnitud in magnitudes[1:]:
    if magnitud[-1] == str(2):
        posicion = float(((float(magnitud[:-2])/0.12566370614359174))+dm1)
        matriz.append('%s.2'%int(round(posicion)))

    if magnitud[-1] == str(3):
        posicion = float(((float(magnitud[:-2])/0.12566370614359174))+dm2)
        matriz.append('%s.3'%int(round(posicion)))    
#tr.salir()
#time.sleep(1)
print matriz

matriz.extend(matriz_prensa)

print matriz
matriz2 = [float(x) for x in matriz]
matriz2.sort()

print "MATRIZ SORTEADA! \n %s"%matriz2 

tr.salir()
time.sleep(1)

try:
    for magnitud in matriz2:
        posicion = str(magnitud)[:-2]
        decoder.SetPoint_posicion(int(posicion))
        print "Avanzando hacia %s..."%(int(posicion))

        while decoder.status:
            time.sleep(0.5)

        if str(magnitud)[-1] == str(2):
            m1.salir()
            time.sleep(3)
            m1.entrar()
            time.sleep(1)
        if str(magnitud)[-1] == str(3):
            m2.salir()
            time.sleep(3)
            m2.entrar()
            time.sleep(1)

        if str(magnitud)[-1] == str(4):
            pr.salir()
            time.sleep(3)
            pr.entrar()
            time.sleep(1)
except KeyboardInterrupt:
    tr.entrar()
    decoder.pid_posicion.motor.parar()
    decoder.cancel()
    decoder.pi.stop()
    decoder.pid_posicion.motor.pi.stop()        

tr.entrar()
decoder.pid_posicion.motor.parar()
decoder.cancel()
decoder.pi.stop()
decoder.pid_posicion.motor.pi.stop()
