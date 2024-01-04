
posicao_maior = maior = None

A = []

for i in range(0, 5):
    A.append(int(input(f'{i + 1}º número: ')))

    if posicao_maior is None or maior is None or A[i] > maior:
        maior = A[i]
        posicao_maior = i


print(f'\nMaior: {maior}     Posição: {posicao_maior + 1}')
