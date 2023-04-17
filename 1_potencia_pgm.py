import numpy as np
import cv2
#Implementar la función de potencia γ, 0 < γ < 2 y γ ̸= 1.

# --- Para imagenes PGM ---
archivo_img = 'Imagenes/TESTpgm.PGM'
# el uso de cv2 se limita a cargar la imagen y numpy para convertirla en un formato que se pueda guardar
def correccion_gamma_pgm(path_image, gamma):
    # cargamos la imagen
    img = cv2.imread(path_image, 0)
    # normalizamos los valores dentro de un rango de valores entre 0 y 255
    img_norm = img / 255.0
    # aplicamos la potencia de gamma 
    img_gamma = img_norm ** gamma
    # desnormalizamos los valores 
    img_gamma_norm = img_gamma * 255
    # pasamos la imagen resultante a un formato guardable 
    img_gamma_norm = np.uint8(img_gamma_norm)
    return img_gamma_norm

# Aplicar la corrección gamma
gamma_corrected_image = correccion_gamma_pgm(archivo_img, 1.7)
original = cv2.imread(archivo_img, cv2.IMREAD_GRAYSCALE)
# Mostrar la imagen original y la imagen corregida gamma
cv2.imshow('Imagen PGM original', original)
cv2.imshow('Imagen PGM corregida gamma', gamma_corrected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()