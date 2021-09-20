# Supongamos que los precios en camion.csv son los precios pagados al productor de frutas mientras que los precios en precios.csv son los precios de venta en el lugar de descarga del camión.

# Ahora vamos calcular el balance del negocio: juntá todo el trabajo que hiciste recién en tu programa informe.py (usando las funciones leer_camion() y leer_precios()) y completá el programa para que con los precios del camión (Ejercicio 2.16) y los de venta en el negocio (Ejercicio 2.17) calcule lo que costó el camión, lo que se recaudó con la venta, y la diferencia. ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.

# los precios del archivo camion.csv representa el costo, y los precios del archivo precios.csv los precios de venta.
# Si multiplicás la cantidad de cajones por el precio de camion.csv, tendrás el costo total.
# Y si multiplicás por los precios de precios.csv tendrás el total ventas.
# Si restás total ventas menos total costo tendrás la utilidad obtenida.
import csv

def leer_precios(nombre_de_archivo):
    with open(nombre_de_archivo) as file:
        rows = csv.reader(file)
        diccionario = {}
        try:
            for row in rows:
                diccionario[row[0]] = float(row[1])
        except IndexError:
            pass
        return diccionario

leer_precios('../Data/precios.csv')


def leer_camion(nombre_de_archivo):
    with open(nombre_de_archivo) as file:
        rows = csv.reader(file)
        headers = next(rows)
        camion = []
        for line in rows:
            d = {
                'nombre': line[0],
                'cajones': int(line[1]),
                'precio': float(line[2])
            }
            camion.append(d)
        return camion

leer_camion('../Data/camion.csv')



def balance(camion, precios):
    costo_camion = 0.0
    total_vendido = 0.0
    for producto in camion:
        prod_nombre = producto['nombre']
        prod_cajones = producto['cajones']
        prod_precio = producto['precio']
        costo_camion += prod_cajones * prod_precio
        if prod_nombre in list(precios):
            total_vendido += prod_cajones * precios[prod_nombre]
    balance = total_vendido - costo_camion
    print(
        f'Costo camion: {costo_camion}, Venta: {total_vendido}, Diferencia: {round(balance, 2)}')
    return balance


balance(
    leer_camion('../Data/camion.csv'),
    leer_precios('../Data/precios.csv')
)

# =======================================================================================================================
# exercise 2

# def leer_camion(nombre_archivo):
#     import csv
#     camion = []

#     with open(nombre_archivo,'rt') as archivo:
#         rows = csv.reader(archivo)
#         headers = next(rows)
#         for row in rows:
#             nombre, cajones, precio = row[0], int(row[1]), float(row[2])
#             camion.append((nombre, cajones, precio))
#     print(camion)

#     costo_total = 0
#     for nombre, cajones, precio in camion:
#         costo_total += cajones*precio
#     print(f'Costo total: {costo_total}')

# leer_camion('../Data/camion.csv')


# def leer_camion(nombre_archivo):
#     import csv
#     from pprint import pprint
#     camion = []

#     with open(nombre_archivo,'rt') as archivo:
#         rows = csv.reader(archivo)
#         headers = next(rows)
#         for row in rows:
#             nombre, cajones, precio = row[0], int(row[1]), float(row[2])
#             diccionario = {
#                 'nombre': nombre,
#                 'cajones': cajones,
#                 'precio': precio
#             }
#             camion.append(diccionario)
#     pprint(camion)

#     costo_total = 0
#     for lote in camion:
#         costo_total += lote['cajones']*lote['precio']
#     print(f'\n Costo total: {costo_total}')

#     return camion

# #leer_camion('../Data/camion.csv')

# def leer_precios(nombre_archivo):
#     import csv
#     from pprint import pprint
    
#     archivo = open(nombre_archivo, 'rt')
#     rows = csv.reader(archivo)

#     listado_frutas = {}
    
#     for row in rows:
#         try:
#             fruta, precio = row[0], float(row[1])
#             listado_frutas[fruta] = precio
#         except:
#             pass
#     archivo.close()
#     print('\n ------------------------------------------------------')
#     print('Listado de precios de frutas: \n')
#     pprint(listado_frutas)

#     return listado_frutas

# def balance(pedido_camion, lista_precios):

#     print('\n ------------------------------------------------------')
#     print('                  INFORME')
#     print(' ------------------------------------------------------ \n')

#     print('Listado del lote pedido:\n')

#     pedido = leer_camion(pedido_camion)
#     listado_precios = leer_precios(lista_precios)

#     costo_pedido = 0
#     total_venta = 0

#     for lote in pedido:
#         for fruta in listado_precios:
#             if lote['nombre'] == fruta:
#                 costo_pedido += lote['cajones']*lote['precio']
#                 total_venta += lote['cajones']*listado_precios[fruta]
#     balance = round(total_venta - costo_pedido,2)
#     print('\n ------------------------------------------------------')
#     print('                  INFORME FINAL')
#     print(' ------------------------------------------------------ \n')

#     print(f'Costo total del pedido: {costo_pedido}')
#     print(f'Total de ingresos por venta: {total_venta}')
#     print(f'Balance: {balance} \n')

# balance(pedido_camion='../Data/camion.csv', lista_precios='../Data/precios.csv')

