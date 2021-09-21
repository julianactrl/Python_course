def busqueda_binaria(lista, x, verbose = False, insertar=False ):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if insertar and pos == -1:
        pos = izq
    return pos


def donde_insertar(lista, x):
    return busqueda_binaria(lista, x, verbose=True, insertar=True)

def insertar(lista, x):
    pos = donde_insertar(lista, x)
    if x in lista:
        pos = pos
    else:
        lista.insert(pos, x)
    return pos


# l = [0,2,4,6]
# print(insertar(l, 3))
# print(l)

