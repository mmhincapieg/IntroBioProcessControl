# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:55:57 2021

@author: aleja
"""

### Importar librerias y funciones que se van a emplear 
import numpy as np # libreria con funciones utiles
import matplotlib.pyplot as plt #funcion para graficar nombrada como plt

# %matplotlib auto # Para graficar en ventanas emergente - copiarlo en la terminal

### Parametros
m = 0.3552 #[kg]
fm = 9.866E-3 #[kg/s]
cp = 1007 #[J/kg*K]
I = 2 #[A]

### Parametros de control
tao = m/fm #[s]
Ku = I/(fm*cp)

### Condicion inicial
T_o = 298.15 #[K]

### Vector tiempo
t_i = 0
t_f = 1000
dt = 0.01
iteraciones = round(t_f/dt) #cantidad de iteraciones a calcular

t = np.linspace(t_i, t_f,(iteraciones+1))

### Entradas (variables)
T_amb = 298.15 #[K]
#V = 50 #[V]
#u = V
d = T_amb # perturbacion

### Parametros del controlador
y_sp = 310.15 #K
Kp = (1/Ku)
Taoi = tao
Taod = 0.1


### Ecuaciones para el metodo de euler
y_e = np.zeros(iteraciones+1)
y_o = T_o
y = y_o

uc_e = np.zeros(iteraciones+1)

d_e = np.zeros(iteraciones+1) #perturbacion

V = 0  #Voltaje [V]
u = V

errorc_e = np.zeros(iteraciones+1)

ysp_e = np.zeros(iteraciones+1)

si=0

for i in range(0, iteraciones+1):
    if t[i] < 200:
        d = 298.15
        y_sp = 305.15
        
    if t[i] > 200 and t[i] < 600:
        d = 278.15
        y_sp = 318.15
        
    if t[i] > 600:
        d = 310.15
        y_sp = 310.15
    
    y_e[i] = y # guarda el valor de la biomasa
    dydt = (-y+Ku*u+d)/tao # calcula el valor de la derivada de y(Temp)
    y = y+dydt*dt # actualiza el valor de la variable segun el metodo de euler
    
    errorc = (y_sp - y)*100/20
    errorc_e[i] = errorc
    ysp_e[i] = y_sp
    si = si+(errorc_e[i]*dt) 
    uc = (Kp*errorc)+((Kp/Taoi)*si)+(Kp*Taod*((errorc-errorc_e[i-1])/dt))# Control proporcional [V]
    if uc > 100:
        uc = 100
                                     
    if uc < 0:
        uc = 0
       
    uc_e[i] = uc
    u = 120*uc/100+0 #guarda el valor del voltaje o variable de salida
    
    d_e[i] = d

### Graficar resultados
plt.figure(7)

## Figura con dos partes
# Parte 1
plt.subplot(311) #amplia figura - '2' filas, '1' columna, grafica '1'ra posicion -
plt.plot(t, y_e, 'r-', label = 'Tincubadora', linewidth = 2) # graficar
plt.ylim(298,323)
plt.plot(t, ysp_e, 'b--', label = 'Ysp', linewidth = 1)
plt.title("Temperatura y voltaje de una incubadora (PI)")
#plt.xlabel('Tiempo[s]')
plt.ylabel('Temperatura [K]')
plt.legend(loc = 'best')
plt.grid(True)

# Parte 2
plt.subplot(312) #amplia figura - '2' filas, '1' columna, grafica '2'da posicion - 
plt.plot(t, uc_e, 'b-', label = "Vincubadora en porcentaje", linewidth = 2)
plt.ylim(0, 105)
# plt.plot(t, Xalg, 'b-', label = 'Xalg') # graficar Xalg
#plt.xlabel('Tiempo [s]')
plt.ylabel('U de control [%]')
plt.legend(loc = 'best')
plt.grid(True)

plt.subplot(313)
plt.plot(t, d_e, 'm-', label='Tamb', linewidth=2)
#plt.ylim(298,323)
plt.xlabel('Tiempo[s]')
plt.ylabel('Tamb [K]')
plt.legend(loc = 'best')
plt.grid(True)

## Grafico del error
plt.figure(8) 
plt.plot(t, errorc_e, 'g-', label = 'Error Tincubadora en porcentaje (PI)')
#plt.ylim(6,12)
plt.title("Error Temperatura de una incubadora en porcentaje")
plt.xlabel('Tiempo [s]')
plt.ylabel('Error Temperatura [%]')
plt.legend(loc = 'best')
plt.grid(True)