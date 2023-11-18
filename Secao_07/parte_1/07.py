

A = []
posicao_maior = maior = None

for i in range(0, 10):

    num = int(input(f'Posição {i + 1}:   '))
    A.append(num)

    if posicao_maior is None or maior is None or num > maior:
        posicao_maior = i + 1
        maior = num

print(f'\nMaior = {maior}')
print(f'Posição do maior = {posicao_maior}')
print(f'Vetor completo: {A}')

# for posicao, elemento in enumerate(A):
#     print(f'{posicao + 1}  -  {elemento}')
