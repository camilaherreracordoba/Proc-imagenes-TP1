import cv2

def negativo_pgm(imagen_pgm, path_negativo):
    with open(imagen_pgm, 'rb') as f:

        cabecera = f.readline()
        ancho, altura = map(int, f.readline().split())
        max_valor = int(f.readline())

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
            valor = max_valor - pixeles[i][j]
            fila.append(valor)
        negativo.append(fila)

    # Guardar la nueva imagen PGM
    with open(path_negativo , 'wb') as f:
        f.write(cabecera)
        f.write('{} {}\n'.format(ancho, altura).encode())
        f.write('{}\n'.format(max_valor).encode())
        for i in range(altura):
            for j in range(ancho):
                f.write(negativo[i][j].to_bytes(1, byteorder='big'))

archivo_img = 'Imagenes/TESTpgm.PGM'
negativo_path = 'Imagenes/NegativoTESTpgm.PGM'
#obtener_negativo(archivo_img, negativo_path)
original = cv2.imread(archivo_img, cv2.IMREAD_GRAYSCALE)
negativo_pgm(archivo_img, negativo_path)
negativo = cv2.imread(negativo_path, cv2.IMREAD_GRAYSCALE)
# Mostrar la imagen original y la imagen negativa
cv2.imshow('Imagen PGM original', original)

cv2.imshow('Imagen PGM negativa', negativo)
cv2.waitKey(0)
cv2.destroyAllWindows()