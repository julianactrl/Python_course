# Datos:

#     Álbum con 670 figuritas.
#     Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
#     Cada paquete trae cinco figuritas.

import random
import numpy as np

# album_vacio = [0,  0,  0,  0,  0,  0]
def crear_album(figus_total):
    return np.zeros(figus_total)

print(crear_album(50))

def album_incompleto(A):
    return 0 in A

print(album_incompleto(crear_album(15)))

def comprar_figu(figus_total):
    return random.randint(1, figus_total)

print(comprar_figu(15))

def cuantas_figus(figus_total = 6):
    contador_figuritas = 0
    album_nuevo = crear_album(figus_total)
    while(album_incompleto(album_nuevo)):
        figuritas = comprar_figu(figus_total)
        contador_figuritas += 1
        album_nuevo[figuritas - 1] += 1
    return contador_figuritas

print(cuantas_figus())

def promedio_figus(figus_total, N):
    promedio = np.mean([cuantas_figus(figus_total) for _ in range(N)])
    print(promedio)

promedio_figus(6, 1000)

def experimento_figus(n_repeticiones, figus_total):
    return np.mean([cuantas_figus(figus_total) for _ in range(n_repeticiones)])

print("Experimento figus: ", experimento_figus(100, 670))