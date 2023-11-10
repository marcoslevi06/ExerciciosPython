
numero = int(input('Digite um número ímpar: '))

if numero % 2 == 0:
    print('Número inválido.')
else:
    for i in range(1, numero + 1, 2):
        print(i)
