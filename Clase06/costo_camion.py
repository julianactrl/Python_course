import informe_funciones



def costo_camion(nombre_archivo):
    costo_total = 0.00

    informe = informe_funciones.leer_camion('../Data/camion.csv')
    for diccionario in informe:
        costo_total += diccionario['cajones'] * diccionario['precio']
    
    return costo_total

print(costo_camion('../Data/camion.csv'))
