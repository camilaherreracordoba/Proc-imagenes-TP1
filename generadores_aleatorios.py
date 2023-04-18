import random
import math
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

from funciones import cargarRAW

#  Gaussiana con desviaci´on standard σ y valor medio µ.
# σ = sigma, µ = mu
def generador_gaussiano(mu, sigma):
    # Generar dos números aleatorios uniformes en el intervalo [0, 1]
    u1 = random.random()
    u2 = random.random()

    # Transformar los números aleatorios a la distribución normal estándar
    z1 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
    z2 = math.sqrt(-2.0 * math.log(u1)) * math.sin(2.0 * math.pi * u2)

    # Transformar los números aleatorios de la distribución normal estándar a la distribución normal deseada
    x = mu + sigma * z1

    return x
def generador_gaussiano_muestras(mu, sigma, n):
    muestras = []
    for i in range(n):
        muestra = generador_gaussiano(mu, sigma)
        muestras.append(muestra)
    return muestras
def rayleigh(xi):
    # Generar un valor uniforme independiente
    u = random.random()

    # Aplicar la transformación inversa para obtener la variable Rayleigh deseada
    x = xi * math.sqrt(-2 * math.log(1 - u))

    return x
def generador_rayleigh(xi, n):
    muestras = []
    for i in range(n):
        muestra = rayleigh(xi)
        muestras.append(muestra)
    return muestras
# lambda es una palabra reservada :p    
def exponencial(lambd):
    # Generar un valor uniforme independiente
    u = random.random()

    # Aplicar la transformación inversa para obtener la variable exponencial deseada
    x = -math.log(1 - u) / lambd
    return x
def generador_exponencial_muestras(lambd, n):
    muestras = []
    for i in range(n):
        muestra = exponencial(lambd)
        muestras.append(muestra)
    return muestras
archivo_img = 'Imagenes/BARCO.RAW'


muestras = generador_gaussiano_muestras(0, 1, 4000)
muestras_rayleigh = generador_rayleigh(1, 2000)
muestras_exponencial = generador_exponencial_muestras(1, 2000)
"""
plt.hist(muestras, bins=50, density=True)
plt.xlabel('x')
plt.ylabel('frecuencia')
plt.title('Distribución Gaussiana')
plt.show()

plt.hist(muestras_rayleigh, bins=50, density=True)
plt.xlabel('x')
plt.ylabel('frecuencia')
plt.title('Distribución Rayleigh')
plt.show()

plt.hist(muestras_exponencial, bins=50, density=True)
plt.xlabel('x')
plt.ylabel('frecuencia')
plt.title('Distribución Exponencial')
plt.show()
# Cargar la imagen raw en escala de grises
#img_raw = np.fromfile(archivo_img, dtype=np.uint8)
"""
"""
img = cargarRAW(290, 207, archivo_img)
cv2.imshow('Imagen RAW original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""