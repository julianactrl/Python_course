from fileparse import parse_csv


# tabla_informe.py
def leer_camion(nombre_archivo):
    return parse_csv(nombre_archivo, select= ['nombre', 'cajones', 'precio'], types = [str, int, float],  has_headers = True)

def leer_precios(nombre_archivo):
    return dict(parse_csv(nombre_archivo, types = [str, float]))

# print(leer_camion('../Data/camion.csv'))
# print(leer_precios('../Data/precios.csv'))

def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], precio_venta, cambio)
        lista.append(t)
    return lista

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in informe:
        print('%10s %10d %10.2f %10.2f' % row)

def informe_camion(camion, precios):
    camion_informe = leer_camion(camion)
    precios_informe = leer_precios(precios)
    informe_general = hacer_informe(camion_informe, precios_informe)
    print_informe = imprimir_informe(informe_general)
    return print_informe
    
# print(informe_camion('../Data/camion.csv', '../Data/precios.csv'))