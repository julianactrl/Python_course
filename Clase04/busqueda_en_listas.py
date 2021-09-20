l = [3, 6, 7, 1, 9, -2]

l2 = [3, 6, -2, 7, 1, 9, -2, -3]

# recorre de izquierda a derecha


def buscar_elem(lista, e):
    i = 0
    pos = -1
    while i < len(lista):
        if lista[i] == e:
            pos = i
            # break corta el ciclo si encontro el primer elemento buscado, sino devuelve la ultima posicion
        i += 1
    return pos


# print(buscar_elem(l2, -2))

# de derecha a izquierda recorre la lista


def buscar_elem2(lista, e):
    p = len(lista) - 1
    # en caso del and envolver con un parentesis las condiciones
    while (p >= 0) and (lista[p] != e):
        p -= 1
    return p

# lo mismo con el for de izq a der


def buscar_elem3(lista, e):
    pos = -1
    for i in range(len(lista)):
        if lista[i] == e:
            pos = i
            break
    return pos
# con for desde der a izq


def buscar_elem4(lista, e):
    pos = -1
    for idx, elem in enumerate(lista):
        if elem == e:
            pos = idx
            break
    return pos

###############################################################################################

def buscar_n_elemento(lista, elemento):
    # contador = lista.count(elemento)
    # print(f'El {elemento} se repite {contador} veces')
    # return contador
    count = 0
    for n in lista:
        print(n)
        if n == elemento:
            count += 1
    # return print(f'el {elemento} se repite {count} veces')


# print(buscar_n_elemento([1, 2, 3, 2, 3, 4, 1, 1], 1))
# print(buscar_n_elemento([1, 2, 3, 2, 3, 4], 2))
# print(buscar_n_elemento([1, 2, 3, 2, 3, 4, 3, 3], 3))

###############################################################################################
def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista.
    if len(lista) > 0:
        m = lista[0]  # Lo inicializo en 0
        for e in lista:  # Recorro la lista y voy guardando el mayor
            if e > m:
                m = e
        return m
    else:
        return None

print(maximo([1, 2, 7, 2, 3, 4]))
print(maximo([1, 2, 3, 4]))
print(maximo([-5, 4]))
print(maximo([-5, -4]))
##############################################################################################
def minimo(lista):    
    if len(lista) > 0:
        menor = lista[0]  
        for e in lista:  
            if e < menor:
                menor = e
        return menor
    else:
        return None

print(minimo([1, 2, 7, 2, 3, 4]))
print(minimo([1, 2, 3, 4]))
print(minimo([-5, 4]))
print(minimo([-5, -4]))