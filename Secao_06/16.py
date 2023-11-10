
numero = int(input('Digite um número ímpar: '))

if numero % 2 == 0:
    print('Número inválido.')
else:
    while 0 <= numero:
        print(numero)
        numero -= 2
