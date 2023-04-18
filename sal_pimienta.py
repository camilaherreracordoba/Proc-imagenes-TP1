import random
import numpy as np
import cv2
from funciones import cargarRAW
def contaminador_img_salypimienta(file, ancho, alto, densidad):
    with open(file, 'rb') as f:
        img = np.fromfile(f, dtype=np.uint8).reshape((alto, ancho))

    n_pixels = int(ancho * alto * densidad)
    indices_salt = random.sample(range(ancho * alto), n_pixels)
    indices_pepper = random.sample(range(ancho * alto), n_pixels)

    img.flat[indices_salt] = 255
    img.flat[indices_pepper] = 0

    with open(file.split('.')[0] + '_salypimienta.raw', 'wb') as f:
        img.tofile(f)

archivo_img = 'Imagenes/LENA.RAW'
img_sp = 'Imagenes/LENA_salypimienta.raw'
this = contaminador_img_salypimienta(archivo_img, 256, 256, 0.01)
img_sp = cargarRAW(256, 256, img_sp)

cv2.imshow('S&P', img_sp)
cv2.waitKey(0)
cv2.destroyAllWindows()