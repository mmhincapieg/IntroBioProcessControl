"""
Created on Tue Nov  9 09:07:15 2021

"""

import numpy as np
import matplotlib.pyplot as plt


# ----------*---------*---------*-----------
          ###Incubadora
# ----------*---------*---------*-----------

#Parametros


cp      = 1007                # Capacidad calorica en J//kg.K
#flujo_m = 9.867E-3
#m      = 0.3552 
flujo_v =  30                 # Flujo volumétrico en m^3/seg
I       = 2                    # Corriente en Amperios
den     = 1.184                   # Densidad del aire
flujo_m = flujo_v * den
V_inc   = 0.3                  # Volumen incubadora en L
m       =  flujo_m   # Masa de Aire en kg


#Condiciones iniciales

t_o = 0
t_f = 600
dt  = 0.01
Temp_o = 298.15                   # Temperatura inicial en Kelvin
Temp_a = 25 + 273.15              # Temperatura ambiental en Kelvin
V = 50                            # Voltaje en voltios


iteraciones = round(t_f/dt)

# Ecuaciones método de Euler

# Parámetros

Tao  = m / flujo_m       # Tiempo de respuesta
Ku   = I/(flujo_m*cp)    # Ganancia
d    = Temp_a


#crear vector del tiempo

t = np.linspace(t_o,t_f,(iteraciones + 1))

# Entradas

u = V
d = Temp_a
Y_sp = 310.15
Y_o = Temp_o


# Asignación de valor inicial

Y = Y_o

# Crear vectores
Yprima   = np.zeros(iteraciones + 1)
uprima   = np.zeros(iteraciones + 1)
e_dif    = np.zeros(iteraciones + 1)
Y_sprima = np.zeros(iteraciones + 1)

#                  APLICACIÓN DEL MÉTODO DE EULER

for i in range(0, iteraciones + 1):
    if t[i] < 300:
        u = 50
    else:
        u = 100
        
    Yprima[i] = Y
    dYdt = (-Y + Ku * u + d)/Tao
    Y = Y + dYdt * dt
    uprima[i] = u
    
    e = Y_sp - Y
    e_dif [i]  = e
    Y_sprima [i] = Y_sp

   
#Graficar resultados


#Parte 1

plt.figure(1)
plt.subplot(211)    #ampliar figura: 1ero es filas, 2ndo es columnas, 3ero es posicion
plt.plot(t, Yprima, color = "lightblue", label = "Temp incubadora", linewidth = 2)
plt.ylim(298,323)   #limitar la temperatura en el rango dado
plt.title("Temperatura y Voltaje de una incubadora")
plt.plot(t, Y_sprima, color = "orange", label = "Set point", linewidth = 1)
plt.ylabel("Temperatura [K] y Voltaje Incubadora")
plt.xlabel("Tiempo [s]")
plt.legend(loc = "best")
plt.grid(True)

#Parte 2

plt.subplot(212)                             
plt.plot(t, uprima, color = "darkgoldenrod", label = "V Incubadora", linewidth = 2)
plt.ylim(0, 120)         #limitar el voltaje en el rango dado
plt.xlabel("Tiempo [seg]")
plt.ylabel("Voltaje [V]")
plt.legend(loc = "best")
plt.grid(True)


#Graficar errror

plt.figure(2)
plt.plot(t, e_dif, color = "steelblue", label = "Error Temp incubadora")
plt.title("Errror de una incubadora")
plt.xlabel("Tiempo [s]")
plt.ylabel("Error Temperatura [K]")
plt.legend(loc = "best")
plt.grid(True)



# ----------*---------*---------*-----------
          ###Migración a variables de proceso
# ----------*---------*---------*-----------

#Parametros


cp      = 1007                 # Capacidad calorica en J//kg.K
flujo_m = 9.867E-3
m       = 0.3552 
flujo_v = 30                   # Flujo volumétrico en m^3/seg
I       = 2                    # Corriente en Amperios
#den     = 1.184               # Densidad del aire
#flujo_m = flujo_v * den
V_inc    = 0.3                 # Volumen incubadora en L
#m       =  flujo_m  # Masa de Aire en kg


#Condiciones iniciales

t_o = 0
t_f = 700
dt  = 0.01
iteraciones = round(t_f/dt)

Temp_o = 298.15                   # Temperatura inicial en Kelvin
Temp_a = 25 + 273.15              # Temperatura ambiental en Kelvin
#V = 50                            # Voltaje en voltios


# Ecuaciones método de Euler

# Parámetros

Tao  = m / flujo_m       #Tiempo de respuesta
Ku   = I/(flujo_m*cp)
d    = Temp_a


#crear vector del tiempo

t = np.linspace(t_o,t_f,(iteraciones + 1))

# Entradas

"""
u = V
"""
d = Temp_a

# Parametros del controlador

Y_sp = 310.15
Kp = 1/Ku

# Asignación de valor inicial

Y_o = Temp_o
Y   = Y_o
V   = 0
u   = V

# Creación vectores


Yprima   = np.zeros(iteraciones + 1)
ucprima  = np.zeros(iteraciones + 1)
ec_dif   = np.zeros(iteraciones + 1)
Y_sprima = np.zeros(iteraciones + 1)
d_prima  = np.zeros(iteraciones + 1)


#                  APLICACIÓN DEL MÉTODO DE EULER

for i in range(0, iteraciones + 1):
    Yprima[i] = Y
    dYdt = (-Y + Ku * u + d)/Tao
    Y = Y + dYdt * dt
    
    ec = (Y_sp - Y)*100/20
    ec_dif [i]  = ec
    Y_sprima [i] = Y_sp
    
    uc = Kp * ec    # Constante proporcional
    
    if uc < 100:
        uc = 100
        
    ucprima[i] = uc
    u = 120 * uc/100+0
    
    d_prima[i] = d
    
    
#Graficar resultados


#Parte 1

plt.figure(3)
plt.subplot(311)    
plt.plot(t, Yprima, color = "lightblue", label = "Temp incubadora PV", linewidth = 2)
plt.ylim(298,323)   
plt.title("Temperatura y Voltaje de una incubadora PV")
plt.plot(t, Y_sprima, color = "orange", label = "Set point", linewidth = 1)
plt.ylabel("Temperatura [K]")
plt.legend(loc = "best")
plt.grid(True)
plt.tight_layout()

#Parte 2

plt.subplot(312)                             
plt.plot(t, ucprima, color = "darkgoldenrod", label = "V Incubadora", linewidth = 2)
plt.ylim(0, 105)         #limitar el voltaje en el rango dado
plt.xlabel("Tiempo [seg]") 
plt.ylabel("Voltaje [V]")
plt.legend(loc = "best")
plt.grid(True)
plt.tight_layout()

#Parte 3

plt.subplot(313)                             
plt.plot(t, d_prima, color = "darkgoldenrod", label = "V Incubadora", linewidth = 2)
plt.ylim(298, 323)         #limitar el voltaje en el rango dado
plt.xlabel("Tiempo [seg]") 
plt.ylabel("Temp amb [K]")
plt.legend(loc = "best")
plt.grid(True)
plt.tight_layout()

#Graficar errror
po
plt.figure(4)
plt.plot(t, ec_dif, color = "steelblue", label = "Error Temp incubadora PV")
plt.title("Errror de una incubadora")
plt.xlabel("Tiempo [s]")
plt.ylabel("Porcentaje rror Temperatura")
plt.legend(loc = "best")
plt.grid(True)
