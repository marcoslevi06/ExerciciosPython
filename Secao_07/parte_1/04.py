

vetor = list()

for i in range(0, 8):
    vetor.append(float(input(f'{i + 1}º: ')))

x = int(input('\nEscolha a posição que deseja para X [Entre 1 e 8]: '))
y = int(input('Escolha a posição que deseja para Y [Entre 1 e 8]: '))

if 1 <= x <= 8 and 1 <= y <= 8:
    soma = vetor[x - 1] + vetor[y - 1]
else:
    print('Inválido.')

# print()
# for indice, elemento in enumerate(vetor):
#    print(f'[{indice}]   -   {elemento}')


print(f'\nSoma das posições [{vetor[x - 1]}] + [{vetor[y - 1]}] = {soma:.2f}')
