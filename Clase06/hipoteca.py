# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
# David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
    
while saldo > 0:
    mes += 1
    if (mes >= pago_extra_mes_comienzo) and (mes <= pago_extra_mes_fin ):
        saldo = saldo * ( 1 + tasa / 12) - pago_mensual - pago_extra 
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        saldo = saldo * ( 1 + tasa / 12 ) - pago_mensual 
        total_pagado = total_pagado + pago_mensual 
        print(mes, round(total_pagado, 2), round(saldo, 2))
    if saldo < pago_mensual:        
        pago_mensual = saldo
        saldo = 0
        total_pagado = total_pagado + pago_mensual 
        mes += 1
print(f'{mes}, {round(total_pagado, 2)}, {saldo}')    
print(f'Total pagado: {round(total_pagado, 2)}')   
print(f'Meses: {mes}') 
#print(mes, round(total_pagado, 2), round(saldo, 2))
#print('Total pagado:', round(total_pagado, 2))
#print('Meses:', mes)


# 1 2684.11 499399.22
# 2 5368.22 498795.94
# 3 8052.33 498190.15
# 4 10736.44 497581.83
# 5 13420.55 496970.98
# ...
# 308 874705.88 3478.83
# 309 877389.99 809.21
# 310 880074.1 -1871.53
# Total pagado:  880074.1
# Meses:  310


# while saldo > 0:
#     mes = mes + 1
#     if mes < 12:
#         saldo = saldo * ( 1 + tasa / 12) - pago_mensual - pago_extra
#         total_pagado = total_pagado + pago_mensual +  pago_extra
#         print('Mes', mes, 'Total pago', round(total_pagado, 2))

# while saldo > 0:
#     if mes <= 12:
# 	    saldo = saldo * (1+tasa/12) - pago_mensual - adelanto
# 	    total_pagado = total_pagado + pago_mensual + adelanto
# 	    mes = mes + 1
# 	    print('Mes:', mes, 'Total pagado:', round(total_pagado,2))
#     else:
# 	    saldo = saldo * (1+tasa/12) - pago_mensual
# 	    total_pagado = total_pagado + pago_mensual
# 	    mes = mes + 1
# 	    print('Mes:', mes, 'Total pagado:', round(total_pagado,2))