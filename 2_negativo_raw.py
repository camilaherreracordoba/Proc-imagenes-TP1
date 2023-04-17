import cv2
from funciones import cargarRAW
def negativo_raw(imagen_raw, negativo_path, ancho, altura):
    with open(imagen_raw, 'rb') as f:
        # Leer los valores de los píxeles
        pixeles = []
        for i in range(altura):
            fila = []
            for j in range(ancho):
                valor = int.from_bytes(f.read(1), byteorder='big')
                fila.append(valor)
            pixeles.append(fila)

    # Calcular el negativo de la imagen
    negativo = []
    for i in range(altura):
        fila = []
        for j in range(ancho):
            valor = 255 - pixeles[i][j]
            fila.append(valor)
        negativo.append(fila)

    # Guardar la nueva imagen RAW
    with open(negativo_path, 'wb') as f:
        for i in range(altura):
            for j in range(ancho):
                f.write(negativo[i][j].to_bytes(1, byteorder='big'))

archivo_img = 'Imagenes/BARCO.RAW'
negativo_path = 'Imagenes/Negativo_BARCO.RAW'
#negativo_raw(archivo_img, negativo_path, 290, 207)
#original = cv2.imread(archivo_img, cv2.IMREAD_GRAYSCALE)
original = cargarRAW(290, 207, archivo_img)

#negativo = cv2.imread(negativo_path, cv2.IMREAD_GRAYSCALE)
negativo = cargarRAW(290, 207, negativo_path)
# Mostrar la imagen original y la imagen negativa
cv2.imshow('Imagen RAW original', original)

cv2.imshow('Imagen RAW negativa', negativo)
cv2.waitKey(0)
cv2.destroyAllWindows()