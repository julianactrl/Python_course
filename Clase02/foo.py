# numero_valido=False
# while not numero_valido:
#     try:
#         a = input('Ingresá un número entero: ')
#         n = int(a)
#         numero_valido = True
#     except ValueError:
#         print('No es válido. Intentá de nuevo.')
# print(f'Ingresaste {n}.')

# numero_valido=False
# while not numero_valido:
#     try:
#         a = input('Ingresá un número entero: ')
#         n = int(a)
#         numero_valido = True
#     except:
#         print('No es válido. Intentá de nuevo.')
# print(f'Ingresaste {n}.')

# raise RuntimeError('¡Qué moco!')

def saludar(nombre):
        'Saluda a alguien'
        print('Hola', nombre)
saludar('juliana')
