#!/usr/bin/env python
import time
import sys
#import rotary_encoder2
import math as m
#from cilindros.cilindro import Sencillo , Doble

largo_prensa = 145
dm1 = 1320 
dm2 = 2250
dpr = 3820
dcz = 6650
distancias = [dm1,dm2,dpr,dcz]
#decoder = rotary_encoder2.decoder( 6, 13,)
'''tr = Doble(0,1)
m1 = Sencillo(2)
m2 = Sencillo(3)
pr = Sencillo(4)
cz = Sencillo(5)
db = Doble(6,7)
'''





magnitudes = sys.argv
print magnitudes
matriz = []
for magnitud in magnitudes[1:]:
    if magnitud[0] == str(1):
    	posicion = float(((float(magnitud[1:])/0.12566370614359174))+dm1)
    	#matriz.append('1%s'%(posicion)
        print posicion #decoder.SetPoint_posicion(posicion+decoder.pos)
        #while decoder.status:
        #    time.sleep(0.5)    	
        #m1.salir()
        #time.sleep(5)
        #m1.entrar()
    if magnitud[0] == str(2):
        #matriz.append('2%s'%(int((int(magnitud[1:])/0.12566370614359174))+dm2))
        posicion = float(((float(magnitud[1:])/0.12566370614359174))+dm2)
    	#matriz.append('1%s'%(posicion)
        print posicion #decoder.SetPoint_posicion(posicion+decoder.pos)
        #while decoder.status:
        #    time.sleep(0.5)
        #m2.salir()
        #time.sleep(5)
        #m2.entrar()
    if magnitud[0] == str(3):
        #matriz.append('3%s'%(int((int(magnitud[1:])/0.12566370614359174))+dpr))            
        posicion = float(((float(magnitud[1:])/0.12566370614359174))+dpr)
    	#matriz.append('1%s'%(posicion)
        print posicion #decoder.SetPoint_posicion(posicion+decoder.pos)
        #while decoder.status:
        #    time.sleep(0.5)
        #pr.salir()
        #time.sleep(5)
        #pr.entrar()
print matriz



print 'hdskjfshdjfkhsdjkfhsdkfkjsdfh'
#magnitudes = magnitudes[1:-1].split(',')
'''magnitudes2 = []
print magnitudes
print magnitudes[1:]
for string in magnitudes[1:]:
    magnitudes2.append(float(string))
print magnitudes2
'''


'''decoder = rotary_encoder2.decoder( 6, 13,)
tr.salir()
time.sleep(0.5)



 
tr.entrar()
decoder.pid_posicion.motor.parar()
decoder.cancel()
decoder.pi.stop()
decoder.pid_posicion.motor.pi.stop()    
'''    
