import csv
ruta = '../Data/arbolado-en-espacios-verdes.csv'


def leer_arboles(nombre_archivo):
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(rows)
        lista_arboles = []
        contador = 0
        for n_fila, fila in enumerate(rows, start=1):
            record = dict(zip(headers, fila))
            record['altura_tot'] = float(record['altura_tot'])
            record['inclinacio'] = float(record['inclinacio'])
            lista_arboles.append(record)

        return lista_arboles

arboleda = leer_arboles(ruta)
# expresion + for  variable + in  iterable
H = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print(len(H))
altura_diametro = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print(len(altura_diametro))

# Sintaxis general

# [<expresión> for <variable> in <secuencia> if <condición>]

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies,arboleda):
    diccionario = { especie: len([(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]) for especie in especies }
    return diccionario

print(medidas_de_especies(especies, arboleda))