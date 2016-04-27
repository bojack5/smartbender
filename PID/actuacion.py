import time
import pigpio
import math as m 

class Actuacion(object):
    """docstring for Actuacion"""
    def __init__(self , gpio):
        self.gpio = gpio
        self.pi = pigpio.pi()
        self.pi.set_mode(self.gpio, pigpio.OUTPUT);

    def ts_2_actuacion(self , tus):
        self.pi.wave_clear()
        self.pi.wave_add_generic([
            pigpio.pulse(0,1<<self.gpio,tus),
            pigpio.pulse(1<<self.gpio,0,tus),])
        wid = pi.wave_create();
        self.pi.wave_send_repeat(wid)

        

"""GPIO=26
velocidad = input('velocidad deseada (mm/s): ')
wid = [0]*10
perimetro = 40*m.pi
dist_p_paso = perimetro/2000
pulsos = velocidad/dist_p_paso
print pulsos
num_ts = 2*pulsos
ts = 1./num_ts       
us = ts*1000000       
pi = pigpio.pi() # Connect to local Pi.
print ts       
pi.set_mode(GPIO, pigpio.OUTPUT);
for i in range(10):
    pi.wave_add_generic([
       pigpio.pulse(0,1<<GPIO,us*(10-(i))),
       pigpio.pulse(1<<GPIO,0,us*(10-(i)))]);
      
    wid[i] = pi.wave_create();
       
pi.wave_chain([
    255, 0,                       # loop start
    wid[0], 
    255, 1, 3, 0, 
    255, 0,                       # loop start
    wid[1],
    255, 1, 3, 0,
    255, 0,                       # loop start
    wid[2],
    255, 1, 3, 0,
    255, 0,                       # loop start
    wid[3],
    255, 1, 3, 0,
    255, 0,                       # loop start
    wid[4],
    255, 1, 3, 0,
    255, 0,                       # loop start
    wid[5],
    255, 1, 3, 0,
    255, 0,                       # loop start
    wid[6],
    255, 1, 3, 0,
    255, 0,                       # loop start
    wid[7],
    255, 1, 10, 0,
    255, 0,                       # loop start
    wid[8],
    255, 1, 3, 0,
    255,0,
    wid[9],    
    255,1,255,0

   ])
      
while pi.wave_tx_busy():
    time.sleep(0.1);
for wave in wid: 
    pi.wave_delete(wave)
 
pi.stop()"""
 
