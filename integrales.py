# Import math Library
import math
import numpy as np

input = np.arange (0,math.pi,0.00001)
print(input)
output = 0
sumariemman=0
dx=0.00001

for x in input:
    output =-( math.cos(x))
    output = output+ output



for x in input:

    area = math.sin(x) * dx

    sumariemman = area + sumariemman

print('valor suma de riemam')
print(sumariemman)



print('valor sumatorio pendientes en el intervalo')
print(output)

print('valor pendiente media')
print(output/math.pi)

print('valor del incremento del valor de y en el intervalo')
print((- math.cos(math.pi) - (- math.cos(0) ) ))
print('valor pendiente entre extremos del intervalo')
resultado =  (- math.cos(math.pi) - (- math.cos(0) ) ) / math.pi
print(resultado)


