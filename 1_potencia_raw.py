import numpy as np
import cv2

archivo_img = 'Imagenes/BARCO.RAW'
gamma = 0.5
def correccion_gamma_raw(image, gamma):
    # Normalizar la imagen entre 0 y 1
    normalized_image = image / 255.0
    # Aplicar la corrección gamma
    #gamma_corrected = np.power(normalized_image, gamma)
    gamma_corrected = normalized_image ** gamma
    # Desnormalizar imagen de vuelta a [0, 255] y convertirla a tipo de datos entero
    gamma_corrected = (gamma_corrected * 255).astype(np.uint8)
    return gamma_corrected

def cargar_imagen_raw(width, height, raw_image_file):
    with open(raw_image_file, 'rb') as file:
        content = file.read()
    raw_image = np.frombuffer(content, dtype=np.uint8)
    # convertir la imagen a una matriz trabajable
    raw_image = raw_image.reshape((height, width))
    return raw_image

# Cargar la imagen RAW en escala de grises
raw_image = cargar_imagen_raw(290, 207, archivo_img)

# Aplicar la corrección gamma a la imagen
gamma_corrected_image = correccion_gamma_raw(raw_image, gamma)

# Mostrar la imagen original y la imagen corregida gamma
cv2.imshow('Imagen RAW original', raw_image)
cv2.imshow('Imagen RAW corregida gamma', gamma_corrected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()