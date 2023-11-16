
maior = None

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        numero = str((i * j))

        if (numero == numero[::-1]):
            # print(f'---> {numero} é palídrono! ')

            if maior is None or int(numero) > maior:
                maior = int(numero)


print(f'\n O maior palídromo é: {maior}')