
import random

A = []
lista_pares = []
lista_impares = []

for i in range(0, 6):
    A.append(random.randint(1, 10))

    if A[i] % 2 == 0:
        lista_pares.append(A[i])
    else:
        lista_impares.append(A[i])


sorted(lista_pares)
sorted(lista_impares)

print(f'\nPares digitados = {lista_pares}')
print(f'Soma dos pares digitados = {sum(lista_pares)}')
print(f'Lista ímpares digitados = {lista_impares}')
print(f'Quantidade de ímpares = {len(lista_impares)}')