# Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso.
# Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones al geringoso
# (como en el Ejercicio 1.18).
# Probá tu función para la lista ['banana', 'manzana', 'mandarina'].
# Guardá este ejercicio en un archivo diccionario_geringoso.py para entregar al final de la clase.

def geringoso(cadena):
    capadepenapa = ''
    for c in cadena:
        capadepenapa += c
        if c in 'aeiou':
            capadepenapa += 'p' + c
    return capadepenapa


def diccionario_geringoso(lista):
    diccionario = {}
    for cadena in lista:
        diccionario[cadena] = geringoso(cadena)
    return diccionario

print(diccionario_geringoso(['banana', 'manzana', 'mandarina']))



# lista = ['banana', 'manzana', 'mandarina']

# ​def geringoso():
#     dic = {}
#     cadena = ''
#     c = ''
#     for s in lista:
#         i = 0
#        for c in s:
#             cadena += c
#                 if c in 'aeiou':
#                     cadena += 'p' + c
#                     dic[s] = cadena
#                     cadena = ''		#print(s[i])
#                     i += 1
# return dic

# ​dic = geringoso()

# print(dic)

