import random

A = []
soma = dp = variancia = 0

for i in range(0, 10):
    A.append(random.randint(5, 10))
    soma += A[i]

media = soma / len(A)

for Xi in A:
    variancia += ((Xi - media)**2) / len(A)

dp = variancia ** 0.5


print(f'Lista = {A}')
print(f'Média: {media}')
print(f'Variância: {variancia:.2f}')
print(f'Desvio Padrão: {dp:.2f}')
