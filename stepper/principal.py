#!/usr/bin/env python
import conf
from stepper import Nema23 , Nema42
def main():
    #Definicion de pines desde archivo conf para Nema 42
    direccion42   = conf.pines['nema42']['direccion']
    pulso42       = conf.pines['nema42']['pulso']
    #Definicion de pines desde archivo conf para Nema 23
    enable23_1    = conf.pines['nema23-1']['enable']
    direccion23_1 = conf.pines['nema23-1']['direccion']
    pulso23_1     = conf.pines['nema23-1']['pulso']

    enable23_2    = conf.pines['nema23-2']['enable']
    direccion23_2 = conf.pines['nema23-2']['direccion']
    pulso23_2     = conf.pines['nema23-2']['pulso']
    




    traccion = Nema42(direccion42,pulso42)
    bolas    = Nema23(enable23_1 , direccion23_1 , pulso23_1)
    flecha   = Nema23(enable23_2 , direccion23_2 , pulso23_2)

    traccion.avance(0,3000,2000)

if __name__ == '__main__':
    main()    		
    
