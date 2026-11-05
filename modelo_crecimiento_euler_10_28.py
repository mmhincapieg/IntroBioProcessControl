### Importar librerias y funciones que se van a emplear 
import numpy as np # libreria con funciones utiles
import matplotlib.pyplot as plt #funcion para graficar nombrada como plt

# %matplotlib auto # Para graficar en ventanas emergente - copiarlo en la terminal

###parametros
mu = 0.7 # velocidad especifica de crecimiento [h^-1]
kd = 0.2 # constante de muerte celular [h^-1]

###condicion inicial
X_o = 0.01 # concentracion inicial de biomasa [g/L]
t_o = 0 # Tiempo inicial [h]
t_f = 10 # Tiempo final [h]
dt = 0.001 # Paso [h] - Cada cuanto tiempo se calcula un punto
iteraciones = round(t_f/dt) #cantidad de iteraciones a calcular

t = np.linspace(t_o, t_f,(iteraciones+1)) # (tiempo inicial, tiempo final, numero de puntos)

### Ecuacion del modelo (Algebraica)
Xalg = X_o*np.exp((mu-kd)*t) #[g/L]

### Ecuacion por el Método de Euler (Ecuacion Diferencial)
X_dif = np.zeros(iteraciones+1) #vector para guardar los valores de cada iteracion
X = X_o #Asigna el valor inicial
for i in range(0, iteraciones+1):
    X_dif[i] = X #guarda el valor de la biomasa
    dXdt = (mu-kd)*X #calcula la derivada de X[g/(h.L)]
    X = X+dXdt*dt #Actualiza el valor de la variable segun el metodo de Euler

### Graficar resultados
plt.figure(1) # abrir figura numero 1
plt.plot(t, Xalg, 'b-', label='Xalg') # graficar Xalg
plt.plot(t,X_dif,'r-',label='Xdif') #graficar X hallado por Euler
plt.title("Cinética de crecimiento microbiano") # titulo de la grafica
plt.xlabel('Tiempo[h]') # marca eje x
plt.ylabel('Biomasa[g/L]') # marca eje y
plt.grid(True) # Muestra las divisiones de los ejes
