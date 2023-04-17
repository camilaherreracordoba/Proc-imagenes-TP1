from funciones import cargarRAW
import cv2
def aplicar_umbral(imagen_raw, ancho, altura, umbral):
    with open(imagen_raw, 'rb') as f:
        # Leer los valores de los píxeles
        pixeles = []
        for i in range(altura):
            fila = []
            for j in range(ancho):
                valor = int.from_bytes(f.read(1), byteorder='big')
                fila.append(valor)
            pixeles.append(fila)

    # Aplicar el umbral a la imagen
    imagen_binaria = [[255 if pixeles[i][j] >= umbral else 0 for j in range(ancho)] for i in range(altura)]

    # Escribir la imagen binaria en un archivo RAW
    nombre_archivo = 'imagen_binaria.raw'
    with open(nombre_archivo, 'wb') as f:
        # Escribir los valores de los píxeles
        for i in range(altura):
            for j in range(ancho):
                f.write(bytes([imagen_binaria[i][j]]))

    return nombre_archivo
archivo_img = 'Imagenes/BARCO.RAW'
umbral = 128
aplicar_umbral(archivo_img, 290, 207, umbral)
imagen_binaria_path = 'imagen_binaria.raw'

img_binaria = cargarRAW(290, 207, imagen_binaria_path)


cv2.imshow('Imagen binaria de umbral', img_binaria)
cv2.waitKey(0)
cv2.destroyAllWindows()