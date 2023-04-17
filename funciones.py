import cv2
import numpy as np 
def cargarRAW (ancho, alto, img):
    with open(img, 'rb') as archivo:
        contenido = archivo.read()
    imagen = np.frombuffer(contenido, dtype=np.uint8)
    imagen = imagen.reshape((alto, ancho))
    imagen = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)
    return imagen  

"""
path = 'Imagenes/Barco.raw'
imgpgm = cv2.imread('negativo.pgm', cv2.IMREAD_GRAYSCALE)
gamma = cargarRAW(290, 207, path)
cv2.imshow("img", gamma)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""