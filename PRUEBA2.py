"""
Created on Thu Nov 19 8:10:54 2021

@author: Maria Manuela
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------*---------*---------*-----------
          ###Simulación tanque de mezclado
# ----------*---------*---------*-----------

#Condiciones iniciales:


t_o  = 0      # tiempo inicial en horas
Ca_f = 1.0    # concentración en primera corriente de alimentación 1 en mol/L
Ca_o = 0.0    # concentración dentro del tanque en mol/L


# Aplicando metodo de Euler

# Parametros

dt  = 0.01
t_f = 10     # tiempo final en horas


iteraciones = round(t_f/dt)

# crear vector del tiempo

t = np.linspace(t_o, t_f, (iteraciones + 1))


# Entradas

Vol  = 100     # volumen del líquido dentro del tanque en m^3
C_a2 = 0.2     # concentracien mol/L
q1   = 50      # flujo volumétrico de corriente 1 en m^3/h
q2   = 50      # flujo volumétrico de corriente 2 en m^3/h
q3   = 100     # flujo volumétrico de la correinte 3 en 100 m^3/h
Ca   = Ca_o

Ca_prima = np.zeros(iteraciones + 1)
Ca_fprima = np.zeros(iteraciones + 1)

for i in range(0, iteraciones+1):
    if t[i] > 6:
        Ca_f = 2
    Ca_prima[i] = Ca
    dCadt = (1 / Vol) * ((q1 * Ca_f) + (q2 * C_a2) - (q3 * Ca)) # Ecuación del modelo
    Ca = Ca + (dCadt * dt)
    Ca_fprima[i] = Ca_f

    
# Graficar resultados

plt.figure(1)

plt.subplot(211)
plt.plot(t, Ca_prima, color = "Coral", label = "Ca", linewidth = 2)
plt.title("Concentración del compuesto A en el tanque")
plt.ylabel("Concentración [mol/L]")
plt.legend(loc = "best")
plt.grid(True)

plt.subplot(212)
plt.plot(t, Ca_fprima, color = "Peru", label = " Ca f", linewidth = 2)
plt.ylabel("Concentración en 1 [mol/L]")
plt.xlabel("Tiempo [h]")
plt.legend(loc = "best")
plt.grid(True)