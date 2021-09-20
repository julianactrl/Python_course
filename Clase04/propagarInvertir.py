# Propagación

lista_1 = [ 0, 0, 0, 1, 0, 0]
lista_2 = [ 0, 0, 0, 0, 0, -1]
lista_3 = [ 0, 0, 0, 0, 0, 1]
lista_4 = []
lista_5 = [ 0 for _ in range(1000) ] + [1]
lista_6 = [1] + [ 0 for _ in range(1000) ]
lista_7 = [ (i% 6)//2-1 for i in range(200) ]
lista_8 = [ -1*((i% 6)//2-1) for i in range(60) ]

def propagar(vector):
    n=len(vector)-1 #largo de la lista -1  
     #recorro de izquierda a derecha
    for i in range(n): #cuanto debo de repetirse el proceso(iterar) 
        if (vector[i]==1) and (vector[i+1]==0): # la posición [i] en vector debe ser igual a 1 y la posición siguiente [i+1] en vector debe ser igual 0 
            vector[i+1]=1 #cambia el valor de la posición i+1 a 1
     #recorro de derecha a izquierda
    for i in range(n): #cuanto debo de repetirse el proceso(iterar)
        if (vector[n-i]==1) and (vector[n-1-i]==0):# la posición [n-i] en vector debe ser igual a 1 y la posición anteior [n-1-i] en vector debe ser igual 0 
            vector[n-1-i]=1 #cambia el valor de la posicion [n-1-i] a 1
    return vector

# def propagar(vector):
#     señal1=0
#     for i,e in enumerate(vector):
#         if vector[i] == 1:
#             señal1 = 1
#         if señal1 == 1:
#             if vector[i] == 0:
#                 vector[i] = 1
#             elif vector[i] == -1:
#                 señal1 = 0
#     return vector

# def invertir_lista(lista):
#     invertida = []
#     for i, e in enumerate(lista, start=1):
#         invertida.append(lista[-i])
#     return invertida

# def propagar_invertir(vector):
    vec=propagar(vector)
    vec1=invertir_lista(vec)
    vec2=propagar(vec1)
    vec3=invertir_lista(vec2)
    return vec3

# vector=[1,0,-1,0,0,1,0,-1,0,0,-1,-1,0,0,1,0,-1,0,1,-1,0,0,0,1,-1]
# print(vector)

# propagacion=propagar_invertir(vector)
# print(propagacion)


print("1", propagar(lista_1))
print("2",propagar(lista_2))
print("3",propagar(lista_3))
print("4",propagar(lista_4))
print("5",propagar(lista_5))
print("6",propagar(lista_6))
print("7",propagar(lista_7))

# print("1: fosforo prendido")
# print("0: fosforo apagado")
# print("-1: fosforo carbonizado")