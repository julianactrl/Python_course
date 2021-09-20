# costo_camion.py

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
#precio de venta - precio de compra

def hacer_informe(camion, precios):
    lista = []
    for producto in camion:
        prod_nombre = producto['nombre']
        prod_cajones = producto['cajones']
        prod_precio = producto['precio']
        precio_de_venta = precios[prod_nombre]
        cambio = precio_de_venta - prod_precio
        tupla = (prod_nombre, prod_cajones, prod_precio, cambio)
        lista.append(tupla)
    
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    
    for nombre, cajones, precio, cambio in lista:
        precio_str = '$' + str(precio)
        
        print(f'{nombre:>10s} {cajones:>10d} {precio_str:>10s} {cambio:>10.2f}')
   


# hacer_informe(leer_camion('../Data/camion.csv'), leer_precios('../Data/precios.csv'))


# import csv
# def leer_camion(nombre_archivo):
#     camion = []
#     total = 0.0
#     f = open(nombre_archivo)
#     rows = csv.reader(f)
#     headers = next(rows)
#     for row in rows:
#         lote = dict(zip(headers, row))
#         try:
#             camion.append(lote)
#             total += int(lote['cajones']) * float(lote['precio'])
#         except ValueError:
#             print('Los datos ingresados de', lote['nombre'], 'se encuentran incompletos')
#     f.close()
#     return camion, total

# def leer_precio(nombre_archivo):
#     productos = []
#     f = open(nombre_archivo)
#     rows = csv.reader(f)
#     for row in rows:
#         try:
#             precio = {'nombre': row[0], 'precio': float(row[1])}
#             productos.append(precio)
#         except IndexError:
#             None
#     f.close()
#     return productos

# def hacer_informe(camion, precios):
#     informe = []
#     headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
#     informe.append(headers)
#     for linea in camion:
#         for row in precios:
#             if row['nombre'] == linea['nombre']:
#                 cambio = float(row['precio']) - float(linea['precio'])
#                 datos = (row['nombre'], int(linea['cajones']), float(linea['precio']), cambio)
#                 informe.append(datos)
#     return informe

# a = leer_camion('../Data/camion.csv')
# costo = a[1]
# camion = a[0]
# venta = 0
# precios = leer_precio('../Data/precios.csv')

# for row in camion:
#     for line in precios:
#         if line['nombre'] == row['nombre']:
#             venta = float(line['precio']) * int(row['cajones']) + venta

# print('El camión costó:', round(costo,2), '$')
# print('Se recaudó con la venta:', round(venta, 2), '$')
# ganancia = venta - costo
# print('Se ganaron', round(ganancia, 2), '$')

# informe = hacer_informe(camion, precios)
# n = 0
# for nombre, cajones, precio, cambio in informe:
#     if n == 0:
#         print(f'{nombre:>10s} {cajones:>10s} {precio:>10s} {cambio:>10s}')
#         print(f'---------- ---------- ---------- ----------')
#     else:
#         pre = '$' + str(precio)
#         print(f'{nombre:>10s}{cajones:>10d}{pre:>10s}{cambio:>10.2f}')
#     n = 1 + n


# import csv
# #%%
# # FUNCION LEER CAMION

# def leer_camion(nombre_archivo):
#     camion = []
#     with open(nombre_archivo, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             lote = {'nombre':row[0], 'cajones':int(row[1]), 'precio':float(row[2])}
#             camion.append(lote)        
#     return camion

# #%%
# # FUNCION LEER PRECIOS

# def leer_precios (nombre_archivo):
#     precios = {}
#     with open(nombre_archivo, 'rt', encoding='utf8') as f:
#         rows = csv.reader(f)
#         for row in rows:
#             try:
#                 precios[row[0]]=float(row[1])
#             except IndexError:
#                print('')
#     return precios
# #%%
# # Hacer informes
# def hacer_informe(camion,precios):
#     filas =[]
#     fila =()
#     cajones=0
#     precio=0.0
#     cambio=0
#     for row in camion:
#         cajones=int(row['cajones'])
#         producto=row['nombre']
#         precio=float(row['precio'])
#         cambio=float(precios[producto]) - precio
#         fila=(producto,cajones,precio,cambio)
#         filas.append(fila)
        
#     return filas


# #%%
# # BALANCES 



# camion = leer_camion('../Data/camion.csv')
# precios = leer_precios('../Data/precios.csv')
# informe = hacer_informe(camion, precios)
# headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
# peso='$'
# print(f'{headers[0]:>10s}{headers[1]:>10s}{headers[2]:>10s}{headers[3]:>10s}')
# print('-'*10,'-'*10,'-'*10,'-'*10)
# for nombre, cajones, precio, cambio in informe:
        
#     print(f'{nombre:>10s} {cajones:>10d} {(peso+str(precio)):>10s} {cambio:>10.2f}')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# '''
# camion = leer_camion('../Data/camion.csv') #llamo a la funcion para traerme el "camion"
# costo_camion= 0.0
# for row in camion:
#         costo_camion += row['cajones']*row['precio']
#         #calculo el costo total del camion
        
# precios = leer_precios('../Data/precios.csv') #me traigo la lista de precios
# venta = 0.0
# for row in camion:
#         producto= row['nombre']
#         venta += row['cajones']*precios[producto]
        
# print('El costo del camión es:  $', costo_camion) 
# print('La venta total es:  $',venta)
# print('La diferencia es:  $', round(venta-costo_camion,2))

# '''
# '''

# Sale un "Warning" porque el archivo "precios.csv" está mal

# Salida:
    
# Warning
# El costo del camión es:  $ 47671.15
# La venta total es:  $ 62986.1
# La diferencia es:  $ 15314.95
# '''
# # %%
