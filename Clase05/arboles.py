import os
import matplotlib.pyplot as plt
from collections import Counter
import csv
import numpy as np


def leer_arboles(nombre_archivo):
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(rows)
        lista_arboles = []
        for n_fila, fila in enumerate(rows, start=1):
            record = dict(zip(headers, fila))
            record['altura_tot'] = float(record['altura_tot'])
            record['inclinacio'] = float(record['inclinacio'])
            lista_arboles.append(record)
        return lista_arboles


def medidas_de_especies(especies,arboleda):
    diccionario = { especie: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies }
    return diccionario

# print(medidas_de_especies())


def scatter_hd(lista_de_pares):
    alt = np.array([altura[0] for altura in lista_de_pares])
    diam = np.array([diametro[1] for diametro in lista_de_pares])
    tamaño = diam.size
    colores = np.random.rand(tamaño)
    area = (15 * np.random.rand(tamaño)) ** 2 
    plt.scatter(diam, alt, s = area, c = colores, alpha = 0.02)
    plt.xlabel('Diametro  (cm)')
    plt.ylabel('Alto (m)')
    plt.xlim = (0,300)
    plt.ylim = (0,60)
    plt.title('Relación diametro - alto para Jacarandás')
    plt.show()

if __name__ == "__main__":
    ruta = '../Data/arbolado-en-espacios-verdes.csv'
    arboleda = leer_arboles(ruta)
    especies = ['Jaracarandá']
    hyd = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá'] 
    plotear_arboles = scatter_hd(hyd)

