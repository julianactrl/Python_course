import numpy as np
import matplotlib.pyplot as plt
import random


def medir_temp(n):
   generar_temp = [random.normalvariate(37.5, 0.2) for _ in range(n)]
   np.save('../Data/temperaturas.npy', generar_temp)
   return generar_temp     

print(medir_temp(999))

def resumen_temp(n):
   temp = medir_temp(n)
   temp_max = max(temp)
   temp_min = min(temp)
   prom = np.mean(temp)
   temp.sort()
   mediana = temp[(n - 1) // 2 ]
   return temp_max, temp_min, prom,  mediana
print(resumen_temp(999))
