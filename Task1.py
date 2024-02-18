import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from queue import Queue

def es_color_similar(pixel, color_objetivo, tolerancia=30):
    return all(abs(pixel[i] - color_objetivo[i]) <= tolerancia for i in range(3))

def es_pared(pixel, umbral):
    return np.all(pixel[:3] <= umbral)  # Ignorar canal alfa si está presente

def es_posicion_valida(pos, forma_laberinto, paredes):
    i, j = pos
    return 0 <= i < forma_laberinto[0] and 0 <= j < forma_laberinto[1] and pos not in paredes

def bfs(laberinto_array, inicio, metas, paredes):
    forma_laberinto = laberinto_array.shape[:2]
    cola = Queue()
    cola.put([inicio])
    visitados = set()
    visitados.add(inicio)

    while not cola.empty():
        camino = cola.get()
        posicion_actual = camino[-1]

        if posicion_actual in metas:
            return camino
        
        for movimiento in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            proxima_posicion = (posicion_actual[0] + movimiento[0], posicion_actual[1] + movimiento[1])
            
            if es_posicion_valida(proxima_posicion, forma_laberinto, paredes) and proxima_posicion not in visitados:
                visitados.add(proxima_posicion)
                cola.put(camino + [proxima_posicion])

    return None

# Cargar la imagen del laberinto
imagen_laberinto = Image.open('Test2.bmp')  
laberinto_array = np.array(imagen_laberinto)

# Definir colores en formato RGB
color_pared = [0, 0, 0]  # Negro
color_inicio = [255, 0, 0]  # Rojo
color_meta = [0, 255, 0]  # Verde
color_camino = [255, 192, 203]  # Rosa para el camino solución

# Identificar el punto de inicio y las metas
posicion_inicio = None
posiciones_meta = []
for i in range(laberinto_array.shape[0]):
    for j in range(laberinto_array.shape[1]):
        if es_color_similar(laberinto_array[i, j], color_inicio):
            posicion_inicio = (i, j)
        elif es_color_similar(laberinto_array[i, j], color_meta):
            posiciones_meta.append((i, j))

# Establecer un umbral para detectar paredes
umbral_pared = 50

# Identificar paredes
conjunto_paredes = set()
for i in range(laberinto_array.shape[0]):
    for j in range(laberinto_array.shape[1]):
        if es_pared(laberinto_array[i, j], umbral_pared):
            conjunto_paredes.add((i, j))

# el inicio y las metas no se consideren paredes
conjunto_paredes.discard(posicion_inicio)
for meta in posiciones_meta:
    conjunto_paredes.discard(meta)

# Encontrar el camino
solucion_camino = bfs(laberinto_array, posicion_inicio, posiciones_meta, conjunto_paredes)

if solucion_camino:
    # Dibujar el camino solución en la imagen
    for posicion in solucion_camino:
        laberinto_array[posicion[0], posicion[1]] = color_camino

    # Convertir el arreglo a imagen y mostrar
    imagen_solucion = Image.fromarray(laberinto_array)
    plt.imshow(imagen_solucion)
    plt.axis('off')
    plt.show()
else:
    print("No se encontró un camino solución.")
