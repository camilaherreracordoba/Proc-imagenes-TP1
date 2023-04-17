import cv2
def aplicar_umbral(imagen_pgm, umbral):
    with open(imagen_pgm, 'rb') as f:
        # Leer la cabecera de la imagen
        cabecera = f.readline().decode('utf-8')
        ancho, altura = map(int, f.readline().decode('utf-8').split())
        max_valor = int(f.readline().decode('utf-8'))

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

    # Escribir la imagen binaria en un archivo PGM
    nombre_archivo = 'imagen_binaria.pgm'
    with open(nombre_archivo, 'wb') as f:
        # Escribir la cabecera de la imagen
        f.write(cabecera.encode())
        f.write('{} {}\n'.format(ancho, altura).encode())
        f.write('{}\n'.format(max_valor).encode())

        # Escribir los valores de los píxeles
        for i in range(altura):
            for j in range(ancho):
                f.write(bytes([imagen_binaria[i][j]]))

    return nombre_archivo

archivo_img = 'Imagenes/TESTpgm.PGM'
img = cv2.imread(archivo_img, cv2.IMREAD_GRAYSCALE)

aplicar_umbral(archivo_img, 64)
imagen_umbral = cv2.imread('imagen_binaria.pgm', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Umbral', imagen_umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()
