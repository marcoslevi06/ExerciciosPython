
while True:
    numero = int(input('Digite um número inteiro entre 100 e 999: '))

    if 100 <= numero <= 999:
        print(numero // 100)
        print((numero % 100) // 10)
        print(numero % 10)
        print('Fim de programa.')
        break
    else:
        continue
