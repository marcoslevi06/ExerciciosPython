
soma_dos_impares = 0

i = int(input('Intervalo inicial: '))
j = int(input('Intervalo final: '))

if i >= j:
    print('Intervalo inválido.')
else:
    for i in range(i, j + 1):
        if i % 2 != 0:
            soma_dos_impares += i


print(f'Soma dos ímpares = {soma_dos_impares}')