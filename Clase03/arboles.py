from collections import Counter
import csv

ruta = '../Data/arbolado-en-espacios-verdes.csv'


def leer_parque(nombre_archivo, parque=''):
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(rows)
        lista_arboles = []
        contador = 0
        for n_fila, fila in enumerate(rows, start=1):
            record = dict(zip(headers, fila))
            record['altura_tot'] = float(record['altura_tot'])
            record['inclinacio'] = float(record['inclinacio'])

            if parque != '':
                if parque == record['espacio_ve']:
                    contador += 1
                    lista_arboles.append(record)
            else:
                lista_arboles.append(record)
        return lista_arboles


parque_gral_paz = leer_parque(ruta, 'GENERAL PAZ')
parque_centenario = leer_parque(ruta, 'CENTENARIO')
parque_los_andes = leer_parque(ruta, 'ANDES, LOS')


def contar_ejemplares(lista_arboles):
    arboles_ejemplares = []
    for arbol in lista_arboles:
        arboles_ejemplares.append(arbol['nombre_com'])
    contador = Counter(arboles_ejemplares).most_common(5)
    dict_arbol = dict(contador)
    print(dict_arbol)


contar_ejemplares(parque_gral_paz)


def obtener_alturas(lista_arboles, especie):
    altura_especie = []
    for altura in lista_arboles:
        if altura['nombre_com'] == especie:
            altura_especie.append(altura['altura_tot'])

    return altura_especie


# Especie: Jacarandá, Parque: Gral Paz
altura_gral_paz_jaca = obtener_alturas(parque_gral_paz, 'Jacarandá')

promedio = sum(altura_gral_paz_jaca) / len(altura_gral_paz_jaca)
print("El promedio de altura es: ", promedio)

alt_max = max(altura_gral_paz_jaca)
print('La altura máxima es: ', alt_max)

# Especie: Jacarandá, Parque: Centenario
altura_centenario_jaca = obtener_alturas(parque_centenario, 'Jacarandá')

promedioCentenario = sum(altura_centenario_jaca) / len(altura_centenario_jaca)
print("El promedio de altura es: ", promedioCentenario)

alt_max_centenario = max(altura_centenario_jaca)
print('La altura máxima es: ', alt_max_centenario)

# Especie: Jacarandá, Parque: Los andes
altura_losandes_jaca = obtener_alturas(parque_los_andes, 'Jacarandá')

promedioLosAndes = sum(altura_losandes_jaca) / len(altura_losandes_jaca)
print("El promedio de altura es: ", promedioLosAndes)

alt_max_losandes = max(altura_losandes_jaca)
print('La altura máxima es: ', alt_max_losandes)




