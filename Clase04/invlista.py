# def invertir_lista(lista):
#     invertida = []
#     n = len(lista) - 1

#     for i in lista:
#         invertida.append(lista[n])
#         n -= 1
    
#     return invertida
    


# print(invertir_lista([1, 2, 3, 4, 5]))
# print(invertir_lista(['Bogotá', 'Rosario',
#       'Santiago', 'San Fernando', 'San Miguel']))

# def invertir_listV2(lista):
#     invertida = []
#     for e in lista:
#         invertida = [e] + invertida
#         print(invertida)

#     return invertida

# print(invertir_listV2([1, 2, 3, 4, 5]))
# print(invertir_listV2(['Bogotá', 'Rosario',
#       'Santiago', 'San Fernando', 'San Miguel']))

def invertir_listaV3(lista):
    invertida=[]
    i = len(lista) -1
    while i >=0:
        invertida.append(lista[i])
        i -= 1
    
    return invertida

print(invertir_listaV3([1, 2, 3, 4, 5]))
print(invertir_listaV3(['Bogotá', 'Rosario',
      'Santiago', 'San Fernando', 'San Miguel']))