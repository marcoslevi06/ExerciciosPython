soma_divisores = 0

numero = int(input('Digite um número: '))

for i in range(1, numero):
    if numero % i == 0:
        print(f'{i}', end=' ')
        soma_divisores += i

print(f'\nSoma dos divisores = {soma_divisores}')
