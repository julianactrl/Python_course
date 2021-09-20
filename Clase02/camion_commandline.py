# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as file:
        acc = 0
        total = 0
        for linea in file:
            linea = linea.rstrip('\n')
            fila = linea.split(',')
            precio = float(fila[2]) 
            acc = precio * int(fila[1])
            total = total + acc
    return total

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)