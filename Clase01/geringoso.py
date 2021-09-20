#Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.
cadena = input("Escribí la palabra que quieras en geringoso: ")

#'Geringoso'
newWord = ''
for str in cadena:
    if str == "a":
        newWord = newWord + 'apa'
    elif str == 'e':
        newWord =newWord + 'epe' 
    elif str == 'i':
       newWord = newWord + 'ipi'
    elif str == 'o':
        newWord = newWord + 'opo'
    elif str == 'u':
        newWord = newWord + 'upu'
    else:
        newWord = newWord + str
    
print(newWord + str)
    

cadena= 'manzana'
capadepenapa = ''
for c in cadena:                                     #para cada letra en cadena:
    if c in 'aeiou':                                 #si la letra es vocal, se le agrega p + la vocal, si no lo es
        capadepenapa= capadepenapa+ c +'p' + c       #se deja como está
    else:
        capadepenapa = capadepenapa + c

print(capadepenapa)

cadena = 'chau'
capadepenapa = ''

for c in cadena: 
    capadepenapa += c
    if c in 'aeiou':
        capadepenapa += 'p' + c
print(capadepenapa)