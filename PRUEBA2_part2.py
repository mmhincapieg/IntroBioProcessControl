"""
Created on Thu Nov 19 8:05:04 2021

@author: Maria Manuela
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# ----------*---------*---------*-----------*-----------
     ###Simulación de un tanque con flujo por gravedad
# ----------*---------*---------*-----------*-----------



# Condiciones iniciales:
    
PV_o = 50         # Apertura inicial de la valvula 
Y_o  = 1          # Nivel inicial del tanque en metros
t_o  = 0          # TIempo inicial en segundos  



# Parametros:
    
A  = 5             # Area del tanque en m^2
g  = 9.81          # Gravedad en m/s^2
Y_sp = 1.5 



# Entradas 
Cv  = 0.0005        # Coeficiente del flujo en m^2/%
V1  = 0.1           # Flujo de entrada del tanque en  m^3/s
dt  = 0.01
t_f = 5000
Y   = Y_o
u   = PV_o   


###               Aplicando el metodo de Euler

iteraciones = round(t_f/dt)
t = np.linspace(t_o, t_f, (iteraciones + 1))


PV_euler = np.zeros(iteraciones + 1)
Y_euler  = np.zeros(iteraciones + 1)
sp_euler = np.zeros(iteraciones + 1)
error_euler = np.zeros(iteraciones + 1)


for i in range(0, iteraciones + 1):
    if t[i] < 750:                       #Modificación en la apertura de la válvula
        u = PV_o
    else:
        u = 70
    Y_euler[i]  = Y
    PV_euler[i] = u
    V2 = u * Cv * np.sqrt(g * Y)         # Flujo de salida del tanque en  m^3/s
    dLdt = (V1/A) - (V2/A)               # Ecuación del modelo
    dYdt = dLdt
    Y = Y + (dYdt * dt)
      
    E1 = Y_sp - Y
    error_euler[i] = E1
    sp_euler[i] = Y_sp
    
"""
print(error, sp)
"""    
    
   
# Graficar resultados

plt.figure(1)
plt.subplot(311)
plt.title("Tanque con flujo por gravedad")
plt.plot(t, Y_euler, color = "steelblue", label = "Nivel Euler", linewidth = 2)
plt.plot(t, sp_euler, color = "midnightblue", label = "Ysp", linewidth = 2)
plt.ylabel("Nivel [m]")
plt.legend(loc = "best")  
plt.grid(True)
plt.tight_layout()

plt.subplot(312)
plt.plot(t, PV_euler, color = "lightsteelblue", label = "Perturbación", linewidth = 2)
plt.ylabel("% Apertura válvula ")
plt.legend(loc = "best")
plt.grid(True)
plt.tight_layout()

plt.subplot(313)
plt.plot(t, error_euler, color = "lightskyblue", label = "Error", linewidth = 2)
plt.xlabel("Tiempo [s]")
plt.ylabel("Error nivel/Ysp=1.5")
plt.legend(loc = "best")
plt.grid(True)
plt.tight_layout()



###            Aplicando RUNGE-KUTTA

# reiniciando valores de entrada
Y   = Y_o
u   = PV_o 

Y_runge = np.zeros(iteraciones + 1)
PV_runge = np.zeros(iteraciones + 1)
sp_runge  = np.zeros(iteraciones + 1)
error_runge = np.zeros(iteraciones + 1)


for i in range(0, iteraciones + 1):
    if t[i] < 750:                       #Modificación en la apertura de la válvula
        u = PV_o
    else:
        u = 70
    Y_runge[i] = Y
    PV_runge[i] = u
    V2 = u * Cv * np.sqrt(g * Y)        # Flujo de salida del tanque en  m^3/s

    k1 = (V1/A) - ((u * Cv * np.sqrt(g * Y))/A)
    k2 = (V1/A) - ((u * Cv * np.sqrt(g * (Y + 0.5 * k1 *dt))/A))
    k3 = (V1/A) - ((u * Cv * np.sqrt(g * (Y + 0.5 * k2 *dt))/A))
    k4 = (V1/A) - ((u * Cv * np.sqrt(g * (Y + k3 *dt))/A))
    
    Y = Y + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
    
    E2 = Y_sp - Y
    error_runge[i] = E2
    sp_runge[i] = Y_sp


"""
print(error, sp_runge)
"""

# Graficar resultados

plt.figure(2)
plt.subplot(311)
plt.title("Tanque con flujo por gravedad")
plt.plot(t, Y_runge, color = "Tomato", label = "Nivel Rugga-Kutta", linewidth = 2)
plt.plot(t, sp_runge, color = "darkorange", label = "Ysp", linewidth = 2)
plt.ylabel("Nivel [m]")
plt.legend(loc = "best")  
plt.grid(True)
plt.tight_layout()

plt.subplot(312)
plt.plot(t, PV_runge, color = "rosybrown", label = "Perturbación", linewidth = 2)
plt.ylabel("% Apertura válvula")
plt.legend(loc = "best")
plt.grid(True)
plt.tight_layout()

plt.subplot(313)
plt.plot(t, error_runge, color = "Tan", label = "Error", linewidth = 2)
plt.xlabel("Tiempo [s]")
plt.ylabel("Error nivel/Ysp=1.5")
plt.legend(loc = "best")
plt.grid(True)
plt.tight_layout()




###            Usando  ODEINT

# Reiniciando valores de entrada

Y   = Y_o
u   = PV_o   

def odin(Y, t):
    V2 = u * Cv * np.sqrt(g * Y)      # Flujo de salida del tanque en  m^3/s
    dYdt = (V1/A) - (V2/A) 
    return dYdt

Y_odin = odeint(odin, Y_o, t)


"""
print(Y_odin)
"""

PV_odin = np.zeros(iteraciones + 1)
spodin  = np.zeros(iteraciones + 1)
error_odin = np.zeros(iteraciones + 1)

for i in range(t_o, iteraciones + 1):
    PV_odin[i] = u
    spodin[i] = Y_sp
    
    E3 = Y_sp - Y_odin[i]
    error_odin[i] = E3
    
"""
print(error_odin, spodin)
"""

# Graficar resultados

plt.figure(3)
plt.subplot(311)
plt.title("Tanque con flujo por gravedad")
plt.plot(t, Y_odin, color = "indianred", label = "Nivel Odeint", linewidth = 2)
plt.plot(t, spodin, color = "crimson", label = "Ysp", linewidth = 2)
plt.ylabel("Nivel [m]")
plt.legend(loc = "best")
plt.grid(True)
plt.tight_layout()

plt.subplot(312)
plt.plot(t, PV_odin, color = "firebrick", label = "Perturbación", linewidth = 2)
plt.ylabel("% Apertura válvula")
plt.legend(loc = "best")
plt.grid(True)
plt.tight_layout()

plt.subplot(313)
plt.plot(t, error_odin, color = "darkred", label = "Error", linewidth = 2)
plt.xlabel("Tiempo [s]")
plt.ylabel("Error nivel/Ysp=1.5")
plt.legend(loc = "best")
plt.grid(True)
plt.tight_layout()


#          GRAFICA COMPARATIVA DE ERRORES:
    
plt.figure(4)
plt.subplot(311)
plt.title("Tanque con flujo por gravedad")
plt.plot(t, error_euler, color = "steelblue", label = "Error euler", linewidth = 2)
plt.legend(loc = "best")
plt.grid(True)
plt.tight_layout()

plt.subplot(312)
plt.plot(t, error_runge, color = "Tan", label = "Error runge", linewidth = 2)
plt.xlabel("Tiempo [s]")
plt.ylabel("Error nivel/Ysp=1.5")
plt.legend(loc = "best")
plt.grid(True)
plt.tight_layout()


plt.subplot(313)
plt.plot(t, error_odin, color = "darkred", label = "Error odeint", linewidth = 2)
plt.xlabel("Tiempo [s]")
plt.legend(loc = "best")
plt.grid(True)
plt.tight_layout()