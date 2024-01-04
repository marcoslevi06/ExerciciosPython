
import random

A = []

for i in range(0, 10):
    A.append(random.randint(0, 1000))


for indice, valor in enumerate(A):
    if valor in[2, 3, 5, 7]:
        print(f'Posição: {indice}       Valor: {valor}')
    else:
        if (valor % 2 != 0) and (valor % 3 != 0) and (valor % 5 != 0) and (valor % 7 != 0):
            print(f'{indice}    {valor}')