#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: 
# El error era de TAL tipo y estaba ubicado en TAL lugar: el contador estaba despues de los return.
# Lo corregí cambiando esto por aquello: se coloco bien el contador, y se saco el else
# A continuación va el código corregido

# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i <= n:
#         if expresion[i] == 'a':
#             return True
#         i += 1
#     return False

# print(tiene_a('UNSAM 2020')) #False
# print(tiene_a('abracadabra')) #False
# print(tiene_a('La novela 1984 de George Orwell')) #True

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.

# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n:
#         if expresion[i] == 'a':
#             return True
#         i += 1
#     return False

# tiene_a('UNSAM 2020')
# tiene_a('La novela 1984 de George Orwell')


#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
def tiene_uno(expresion):
    try:
        n = len(expresion)
        i = 0
        tiene = False
        while (i<n) and not tiene:
            if expresion[i] == '1':
                tiene = True
            i += 1
        return tiene
    except TypeError:
        return print('Acepta solo str')

print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
tiene_uno(1984)


# %%

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

# a = [1, 2 , 3]
# b = a
# a = [4, 5, 6]
# print(a, b)
# %%
