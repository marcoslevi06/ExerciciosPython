


# Faça um programa que encontre o primeiro múltiplo de 11, 13 ou 1 após um número dado.

numero = int(input('Digite um número: '))

while True:
    print(numero)

    if numero % 11 == 0:
        print(f'Primeiro múltiplo de 11 após número informado é: {numero}')
        break
    if numero % 13 == 0:
        print(f'Primeiro múltiplo de 13 após número informado é: {numero}')
        break
    if numero % 17 == 0:
        print(f'Primeiro múltiplo de 17 após número informado é: {numero}')
        break
    
    numero += 1
