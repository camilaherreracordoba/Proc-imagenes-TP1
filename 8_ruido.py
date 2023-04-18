from generadores_aleatorios import generador_gaussiano_muestras, generador_rayleigh, generador_exponencial_muestras
from funciones import cargarRAW
import cv2
import numpy as np
import random


def contaminar_imagen_gaussiana(filename, width, height, percentage, mu, sigma):
    # Cargar la imagen RAW en escala de grises como una matriz NumPy
    with open(filename, 'rb') as f:
        img = np.fromfile(f, dtype=np.uint8).reshape((height, width))

    # Calcular el número de píxeles a contaminar
    n_pixels = int(width * height * percentage)

    # Generar una lista de índices aleatorios para los píxeles a contaminar
    indices = random.sample(range(width * height), n_pixels)

    # Generar una lista de valores de ruido gaussiano
    ruido = generador_gaussiano_muestras(mu, sigma, n_pixels)

    # Crear una matriz de ruido con los valores generados
    ruido = np.array(ruido).reshape((-1, 1))

    # Contaminar los píxeles seleccionados con el ruido gaussiano generado
    ruido_convertido = np.clip(np.round(ruido), 0, 255).astype(np.uint8)
    img.flat[indices] += ruido_convertido.flatten()
    #img.flat[indices] += ruido.flatten()

    # Guardar la imagen contaminada como un archivo RAW
    with open(filename.split('.')[0] + '_gaussiano.raw', 'wb') as f:
        img.tofile(f)
def contaminador_img_rayleigh(file, ancho, alto, porcentaje, xi):
    with open(file, 'rb') as f:
        img = np.fromfile(f, dtype=np.uint8).reshape((alto, ancho))

    n_pixels = int(ancho * alto * porcentaje)
    indices = random.sample(range(ancho * alto), n_pixels)

    ruido = generador_rayleigh(xi, n_pixels)

    ruido = np.array(ruido).reshape((-1, 1))
    ruido_convertido = np.clip(np.round(ruido), 0, 255).astype(np.uint8)
#    img.flat[indices] *= ruido_convertido.flatten()
    img.flat[indices] = img.flat[indices] * ruido.flatten()
    with open(file.split('.')[0] + '_rayleigh.raw', 'wb') as f:
        img.tofile(f)
def contaminador_img_exponencial(file, ancho, alto, porcentaje, lambd):
    with open(file, 'rb') as f:
        img = np.fromfile(f, dtype=np.uint8).reshape((alto, ancho))

    n_pixels = int(ancho * alto * porcentaje)
    indices = random.sample(range(ancho * alto), n_pixels)

    ruido = generador_exponencial_muestras(lambd, n_pixels)

    ruido = np.array(ruido).reshape((-1, 1))
    ruido_convertido = np.clip(np.round(ruido), 0, 255).astype(np.uint8)
    img.flat[indices] *= ruido_convertido.flatten()
    with open(file.split('.')[0] + '_exponencial.raw', 'wb') as f:
        img.tofile(f)

archivo_img = 'Imagenes/LENA.RAW'
mu = 0
sigma = 20
contaminar_imagen_gaussiana(archivo_img, 256, 256, 0.7, mu, sigma)
img_contaminada = 'Imagenes/LENA_gaussiano.raw'
#cv2.imshow('Gaussiano', img_contaminad)
img_contaminada = cargarRAW(256, 256, img_contaminada)
cv2.imshow('Gaussiano', img_contaminada)

contaminador_img_rayleigh(archivo_img, 256, 256, 0.3, 1)
rayleigh_img = 'Imagenes/LENA_rayleigh.raw'
rayleigh_img = cargarRAW(256, 256, rayleigh_img)
cv2.imshow('Rayleigh', rayleigh_img)

contaminador_img_exponencial(archivo_img, 256, 256, 0.3, 1)
exp_img = 'Imagenes/LENA_exponencial.raw'
exp_img = cargarRAW(256, 256, exp_img)
cv2.imshow('Exponencial', exp_img)
img = cargarRAW(256, 256, archivo_img)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()