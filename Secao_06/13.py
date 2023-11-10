

numero = int(input('Digite um número par: '))

if numero % 2 != 0:
    print('Número inválido.')
else:
    for i in range(0, numero + 1, 2):
        print(i)
