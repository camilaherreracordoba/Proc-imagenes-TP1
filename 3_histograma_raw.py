import matplotlib.pyplot as plt

def histograma_raw(imagen_raw, ancho, altura):
    with open(imagen_raw, 'rb') as f:
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

    return conteos

def graficar_histograma_raw(imagen_raw, ancho, altura):
    conteos = histograma_raw(imagen_raw, ancho, altura)
    plt.bar(range(256), conteos)
    plt.title('Histograma de niveles de gris')
    plt.xlabel('Nivel de gris')
    plt.ylabel('Frecuencia')
    plt.show()

archivo_img = 'Imagenes/BARCO.RAW'

graficar_histograma_raw(archivo_img, 290, 207)
