import conf
import time
from cilindro import Sencillo , Doble

def main():
    traccion = Doble(0,1)
    muesca1  = Sencillo(2)
    muesca2  = Sencillo(3)
    prensa   = Sencillo(4)
    cizalla  = Sencillo(5)
    dobladora= Doble(6,7)

    for i in range(10):
    	print 'Vuelta : %s'%(i+1)
        traccion.salir()
        time.sleep(1)
        print bin(conf.estado)
        traccion.entrar()
        time.sleep(1)
        print bin(conf.estado)
        traccion.reset()
        time.sleep(1)
        print bin(conf.estado)  
        muesca1.salir()
        time.sleep(1)
        print bin(conf.estado)
        muesca1.entrar()
        time.sleep(1)
        print bin(conf.estado)
        muesca2.salir()
        time.sleep(1)
        print bin(conf.estado)
        muesca2.entrar()
        time.sleep(1)
        print bin(conf.estado)
        prensa.salir()
        time.sleep(1)
        print bin(conf.estado)
        prensa.entrar()
        time.sleep(1)
        print bin(conf.estado)
        cizalla.salir()
        time.sleep(1)
        print bin(conf.estado)
        cizalla.entrar()
        time.sleep(1)
        print bin(conf.estado)
        dobladora.salir()
        time.sleep(1)
        print bin(conf.estado)
        dobladora.entrar()
        time.sleep(1)
        print bin(conf.estado)
        dobladora.reset()
        time.sleep(1)
        print bin(conf.estado)

if __name__ == '__main__':
	main()





