#----------------------------------------------
#Cordero Correa Victor Hugo
#-----------------------------------------------



import matplotlib.pyplot as plt
import numpy as np

#---------------------------------------
#Genera datos de prueba
#---------------------------------------
mm = 3.0
bb = 5.0
x = np.linspace(0.0,1.0,400,dtype=np.float32)
e = np.random.normal(0,1,400)
y = mm*x+bb+e

x1 = np.linspace(1.0,2.0,20,dtype=np.float32) 
e1 = np.random.normal(0,0.1,20)
y1 = mm*x1+bb + e1

m = 0
b = 0

#--------------------------
#Tasa de aprendizaje
#--------------------------
L = 0.1

#------------------------------------
#Iteraciones
#------------------------------------
epochs = 200

#-----------------------------------------------------
#Minimizar caminando por la direccion - gradiente
#------------------------------------------------------
n = float(len(x))
for i in range(epochs):
  Y_pred = m*x + b # Prediccion de Y
  D_m = (-2.0/n) * sum(x * (x - Y_pred)) #Derivada parcial con m
  D_b = (-2.0/n) * sum(x * (y - Y_pred)) #Derivada parcial con b
  m = m - L * D_m #Mejorar m
  b = b - L * D_b # Mejorar b

print(m, b)
yy = m*x1+b
#-------------------------
#Graficas
#-------------------------
plt.scatter(x1, y1, color="red")
plt.plot(x1, yy, color="black", linewidth=1)

plt.show()