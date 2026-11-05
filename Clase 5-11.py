import numpy as np
import matplotlib.pyplot as plt

# ----------*---------*---------*-----------
          ###Clase 6 solución de ecuaciones
# ----------*---------*---------*-----------

# Parámetros

miu = 0.7 #velocidad
kd = 0.2 #cte muerte


#Condiciones iniciales

X_o = 0.01 
t_o = 0
t_f = 10
dt =0.1
iteraciones = round(t_f/dt)


#crear vector del tiempo

t = np.linspace(t_o,t_f,(iteraciones + 1))

X = X_o * np.exp((miu - kd) * t)  #ecuación del modelo


# Graficar resultados

plt.figure(1) #abrir figura
plt.plot(t, X) #graficar
plt.title("Cinética de crecimiento microbiano analítica")
plt.xlabel("Tiepo [h]") 
plt.ylabel("Biomasa [g/L]")
plt.grid(True) #saca divisiones de los ejes

# ----------*---------*---------*-----------
          ###Clase 7 Método de euler
# ----------*---------*---------*-----------



Xalg = X_o * np.exp((miu - kd)*t)

X_dif = np.zeros(iteraciones+1)

X = X_o

for i in range(0, iteraciones+1):
    X_dif[i] = X
    dXdt =(miu - kd)*X
    X = X + dXdt * dt
    
#Gráficar resultados

plt.figure(1)
plt.plot(t,Xalg, "b-", label = "Xalg")
plt.plot(t, X_dif, "r-", label = "Xdif")
plt.title("Cinética de crecimiento microbiano con método de Euler")
plt.xlabel("Tiempo [h]")
plt.ylabel("Biomasa [g/L]")
plt.legend(loc = "best")
plt.grid(True)