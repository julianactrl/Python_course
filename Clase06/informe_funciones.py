from fileparse import parse_csv
camion = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float],  has_headers = True)
print(camion)

# tabla_informe.py
import csv

def leer_camion(nombre_archivo):
    '''
    Lee un archivo de lotes en un camión 
    y lo devuelve como lista de diccionarios con claves
    nombre, cajones, precio.

    '''
    camion = []
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            cajon = {
                'nombre' : record['nombre'],
                'cajones' : int(record['cajones']),
                'precio' : float(record['precio'])
            }
            camion.append(cajon)
    return camion