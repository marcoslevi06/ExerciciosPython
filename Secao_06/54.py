

while True:
    numero = int(input('\nDigite um inteiro positivo: '))

    if numero <= 1:
        print('Número inválido.')
    else:
        if numero in (2, 3, 5, 7):
            print('Número primo.')
            break

        if numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0:
            print('Número primo.')
            break

        print('Número NÃO é primo.')
        break
