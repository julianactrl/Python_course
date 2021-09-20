import csv

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
    print(total)
    return total

costo = costo_camion('../Data/camion.csv')
print('Costo total: $', costo)


def costo_camion1(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    total = 0.0

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        # headers = next(rows)
        for row in rows:
            ncajones = int(row[1])
            precio = float(row[2])
            total += ncajones * precio
    print('Total: $', total)
    return total

print(costo_camion1('../Data/camion.csv'))