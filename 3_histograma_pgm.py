import cv2
import matplotlib.pyplot as plt

def histograma_pgm(imagen_pgm):
    with open(imagen_pgm, 'rb') as f:
        # Leer la cabecera de la imagen PGM
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

    # Contar la cantidad de veces que aparece cada nivel de gris
    conteos = [0] * 256
    for i in range(altura):
        for j in range(ancho):
            conteos[pixeles[i][j]] += 1

    # Mostrar el gráfico del histograma
    plt.bar(range(256), conteos)
    plt.title('Histograma de niveles de gris')
    plt.xlabel('Nivel de gris')
    plt.ylabel('Frecuencia')
    plt.show()
archivo_img = 'Imagenes/TESTpgm.PGM'
img = cv2.imread(archivo_img, cv2.IMREAD_GRAYSCALE)
histograma_pgm(archivo_img)
