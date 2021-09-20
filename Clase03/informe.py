# costo_camion.py

import csv

def costo_camion(nombre_archivo):

    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        encabezados = next(rows)

        costo_total = 0.00
        for n_fila, fila in enumerate(rows, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            except ValueError:
                print(f'Fila {n_fila + 1}: No pude interpretar: {fila}')
        return costo_total

print(costo_camion('../Data/camion.csv'))
print(costo_camion('../Data/missing.csv'))
print(costo_camion('../Data/fecha_camion.csv'))

########################################################################################
