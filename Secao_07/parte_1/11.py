# Usarei para gerar os número e não precisar ficar digitando toda hora que testar

import random

A = []
total_negativos = soma_positivos = 0

while len(A) < 10:
    # dá pra determinar o intervalo de flutuantes através dos parêmetros do uniform
    # se for inserir a entrada, apenas mudar para um input()
    num = random.uniform(-10, 10)
    A.append(num)

    if num < 0:
        total_negativos += 1

    if num > 0:
        soma_positivos += num


print(f'\nVetor completo = {A}')

print(f'\nQuantidade de números negativos = {total_negativos}')
print(f'Soma dos positivos = {soma_positivos:.2f}')
