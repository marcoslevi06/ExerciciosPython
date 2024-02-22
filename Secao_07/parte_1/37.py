import random

vetor = [1.3, 1.5, 2.5, 1, 2.5, 2.5, 2.2, 5.5, 4.5, 4.5, 0.5]
temp = 0

for i in range(0, len(vetor)):
    if i < 6:
        for j in range(0, 6):
            if vetor[i] < vetor[j]:
                temp = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = temp
    else:
        for j in range(6, len(vetor)):
            if vetor[i] > vetor[j]:
                temp = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = temp

print(f'Vetor: {vetor}')

for posicao, valor in enumerate(vetor):
    if posicao == 6:
        print()

    print(f'{posicao + 1}   {valor}')