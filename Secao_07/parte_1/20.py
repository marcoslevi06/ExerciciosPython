
# Vou usar random para preencher o vetor

import random

A = []
impares = []
i = 0

while len(A) < 10:

    A.append(random.randint(0, 50))

    if A[i] % 2 != 0:
        impares.append(A[i])

    i += 1


# print(f'\nVetor completo: {A}')
# print(f'Apenas os ímpares = {impares}')


# imprimindo dois por vez como a questão pede
cont_linha = 0

print('\nTODOS OS NÚMEROS: ')

for i in A:
    cont_linha += 1
    print(f'{i}', end=' ')

    if cont_linha == 2:
        cont_linha = 0
        print()


cont_linha = 0
print('\nAPENAS OS NÚMEROS ÍMPARES: ')
for i in impares:
    cont_linha += 1
    print(f'{i}', end=' ')

    if cont_linha == 2:
        cont_linha = 0
        print()
