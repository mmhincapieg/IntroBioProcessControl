import numpy as np
import matplotlib.pyplot as plt

# ----------*---------*---------*-----------
     ### Reto 1: Bier Oscilaciones Glucoliticas
# ----------*---------*---------*-----------


# Parametros

v_glu = 0.36
k1 = 0.02
k2 = 6
km = 13
dt = 0.01

# Condiciones iniciales

G_o =  4
ATP_o = 3
t_o = 0
t_f = 700

iteraciones = round(t_f/dt)



t = np.linspace(t_o , t_f , (iteraciones + 1) )
ATP_euler = np.zeros(iteraciones + 1)
G_euler = np.zeros(iteraciones + 1)



ATP = ATP_o
G = G_o


for i in range(0, iteraciones + 1):
    ATP_euler [i] = ATP
    G_euler [i] = G
    dGdt = v_glu - (k1 * G * ATP)
    dAdt = 2 * k1 * G * ATP - (k2 * ATP / (km + ATP))
    ATP = ATP + dAdt  * dt
    G = G + dGdt * dt


# ----------*---------*---------*-----------
     ### Gráfica
# ----------*---------*---------*-----------

plt.figure(1)
plt.plot(t, ATP_euler, color = "orange", label = "ATP")
plt.plot(t, G_euler, color = "skyblue", label = "Glucosa")
plt.title("Oscilaciones en la Glucolisis")
plt.xlabel("Tiempo [s]")
plt.ylabel("Concentración [nM]")
plt.legend(loc = "best")
plt.grid(True)