# estados nuevo = 0
# estado encendido = 1
# estado carbonizado = -1
# los quedamos no pueden revertir su estado

lista_1 = [ 0, 0, 0, 1, 0, 0]
lista_2 = [ 0, 0, 0, 0, 0, -1]
lista_3 = [ 0, 0, 0, 0, 0, 1]
lista_4 = []
lista_5 = [ 0 for _ in range(1000) ] + [1]
lista_6 = [1] + [ 0 for _ in range(1000) ]
lista_7 = [ (i% 6)//2-1 for i in range(200) ]
lista_8 = [ -1*((i% 6)//2-1) for i in range(60) ]

def propagar(lista):
    n = len(lista) - 1
    m = len(lista) - 1
    
    copy = lista.copy()

    for index, value in enumerate(copy):
        # si el valor es igual a uno, y si el value del siguiente es menor al largo de la lista y si el valor del siguiente es igual a cero que sea uno
        if (value == 1) and (index + 1 <= n) and (copy[index + 1] == 0):
            copy[index + 1] = 1

        if (m >= 0) and (copy[m] == 1) and (copy[m - 1] == 0):
            copy[m - 1] = 1
        m -= 1

    return copy


# print(propagar([0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]))
# print(propagar([0, 0, 0, 1, 0, 0]))
print("1", propagar(lista_1))
print("2",propagar(lista_2))
print("3",propagar(lista_3))
print("4",propagar(lista_4))
print("5",propagar(lista_5))
print("6",propagar(lista_6))
print("7",propagar(lista_7))








# def propagaV2(lista):
#     for i, f in enumerate(lista):
#         if i - 1 >= 0:
#             if f == 0 and lista[i - 1] == 1:
#                 lista[i] = 1
#         if i + 1 < len(lista):
#             if f == 0 and lista[i+1] == 1:
#                 lista[i] = 1

#     return lista


# # print(propagaV2([0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]))
# print(propagaV2([0, 0, 0, 1, 0, 0]))