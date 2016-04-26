import time

class Encoder(object):
    """docstring for Encoder"""
    def __init__(self, arg):
        super(Encoder, self).__init__()
        self.arg = arg

    def vel2pulsos( velocidad , distancia):
        perimetro = 125.66370614359172 #mm
        pulsos = velocidad * 2000 / perimetro
        slp = 1./(2*pulsos)
        pasos = (distancia/perimetro)*2000
        print round(pasos)
        print "Funcionando a una velocidad de %s mm/s \t a %s pulsos cada segundo."%(velocidad,pulsos)
        cuenta = 0
        t1 = time.clock()
        try:
            for i in xrange(0,int(round(pasos))):
                #GPIO.output(self.pin_pulse,False)
                cuenta += 1
                time.sleep(slp)
                #GPIO.output(self.pin_pulse,True)
                time.sleep(slp)
            t2 = time.time()    
            print "Se dieron %s pasos , deberian de ser %s en %s segundos" % (cuenta , pasos , t2-t1)
            




        except KeyboardInterrupt:
            print "Terminado de girar"
            #GPIO.cleanup()


class Nema42(object):
    """docstring for Nema42"""
    def __init__(self):
        self.perimetro = 125.66370614359172
        self.dist_x_pulso = self.perimetro/2000

    def ts_from_vel(self , velocidad):
        num_pulsos = velocidad/self.dist_x_pulso
        ts = 1./(2*num_pulsos)

        return ts


            


        
        
def pulsos2vel():
    pass
def procedure():
    time.sleep(2.5)
# measure process time
t0 = time.clock()
procedure()
print time.clock() - t0, "seconds process time"

# measure wall time
t0 = time.time()
procedure()
print time.time() - t0, "seconds wall time"        


procedure()

#vel2pulsos(10,10)
