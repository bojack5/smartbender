#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

filename = "prbs_ampli_multiple1s.log"

with open(filename) as f:
    header = f.readline().split("\t")
    
data = np.genfromtxt(filename , delimiter = '\t' , skip_header = 1 , 
	                 names = ['corrida' , 'velocidad' , 'posicion' ,])

fig = plt.figure(1)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(data['corrida'] , data['velocidad'] ,'g')

ax2.plot(data['corrida'] , data['posicion'] , 'r')

ax1.set_title("Prueba PRBS para PID de posicion")
ax1.set_xlabel('Corrida')
ax1.set_ylabel('Velocidad')

ax2.set_xlabel('Corrida')
ax2.set_ylabel('posicion')

leg1 = ax1.legend()
leg2 = ax2.legend()

plt.show()
