import csv

def buscar_precio(fruta):
    with open('Data/precios.csv') as f:  # lectura del file
        rows = csv.reader(f)
        fruta_encontrada = ''
        precio = 0
        for row in rows:
            if(fruta == row[0]):
                fruta_encontrada = row[0]
                precio = row[1]
            
    
    if(fruta_encontrada != ''):    
        print(f'El precio de un cajón de {fruta_encontrada} es: $', precio)
    else:
        print(f'{fruta_encontrada} no figura en el listado de precios.')

buscar_precio('Lima')
buscar_precio('Frutilla')
buscar_precio('Uva')

