#!/usr/bin/env python
import time
import sys
import rotary_encoder2
import math as m
from cilindros.cilindro import Sencillo , Doble


tr = Doble(0,1)
m1 = Sencillo(2)
m2 = Sencillo(3)
pr = Sencillo(4)
cz = Sencillo(5)
db = Doble(6,7)

largo_prensa = 145
dm1 = 1320
dm2 = 2250
dpr = 3820
dcz = 6650

magnitudes = sys.argv
print magnitudes
#magnitudes = magnitudes[1:-1].split(',')
magnitudes2 = []
print magnitudes
print magnitudes[1:]
for string in magnitudes[1:]:
    magnitudes2.append(float(string))
print magnitudes2


decoder = rotary_encoder2.decoder( 6, 13,)
tr.salir()
time.sleep(0.5)

try:

    for magnitud in magnitudes2:
        print magnitud
        print "Cortando Magnitud de %s"%magnitud
        veces = m.ceil(magnitud/largo_prensa)
        print "Magnitud cortada en %s partes"%veces
        for paso in range(int(veces)):
            avance = (int((float(magnitud))/(veces))/0.12566370614359174)
            decoder.SetPoint_posicion(int(avance+decoder.pos))
            print "distancia a recorrer = %s"%(int(avance))
            print "Moviendose hacia %s "%(int(avance+decoder.pos))
            while decoder.status:
                time.sleep(0.5)
            print "Motor Parado..."
            m2.salir()
            time.sleep(5)
            m2.entrar()
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
    
