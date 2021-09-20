#TABLA DE MULTIPLICAR

print(' '*5, end='')
for headers in range(0, 10):                #  encabezados
    print (f'{headers:>4d}', end='')       
print() 
print('-'*(45), end='') 
print() 

for rows in range(0, 10):              
    print(f'{rows:>4d}:', end='')
    for calculate in range(0, 10):
        result = rows * calculate
        print(f'{result:>4d}', end='')
    print ('')


suma=0
tabla=[]
a=[]
e=[]
for x in range(0,10):
    for y in range(0,10):
        tabla.append(suma)
        suma+=x
    suma=0
    a.append(tabla)
    tabla=[]
    e.append(x)
print(f'{e[0]:>3d} {e[1]:>3d} {e[2]:>3d} {e[3]:>3d} {e[4]:>3d} {e[5]:>3d} {e[6]:>3d} {e[7]:>3d} {e[8]:>3d} {e[9]:>3d}')
print('-'*39)
for i in a:
    print(f'{i[0]:>3d} {i[1]:>3d} {i[2]:>3d} {i[3]:>3d} {i[4]:>3d} {i[5]:>3d} {i[6]:>3d} {i[7]:>3d} {i[8]:>3d} {i[9]:>3d}')