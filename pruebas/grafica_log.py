#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

filename = "datos_pid_posicion_var.log"

with open(filename) as f:
    header = f.readline().split("\t")
    
data = np.genfromtxt(filename , delimiter = '\t' , skip_header = 1 , 
	                 names = ['corrida' , 'SetPoint' , 'Posicion' ,])

fig = plt.figure(1)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(data['corrida'] , data['SetPoint'] ,'g')

ax2.plot(data['corrida'] , data['Posicion'] , 'r')

ax1.set_title("Grafica Posicion ")
ax1.set_xlabel('Corrida')
ax1.set_ylabel('SetPoint')

ax2.set_xlabel('Corrida')
ax2.set_ylabel('posicion')

leg1 = ax1.legend()
leg2 = ax2.legend()

plt.show()
