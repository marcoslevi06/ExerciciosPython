

def soma_numeros(numero1: int, numero2: int):

    cont = 0

    if numero1 == numero2:
        return 'Distância é zero. Números são iguais.'
    elif numero1 > numero2:
        maior = numero1
        menor = numero2
    else:
        maior = numero2
        menor = numero1

    for i in range(menor + 1, maior):
        print(f'Números de {menor} até {maior}: {i}')
        cont += i

    return cont


a = int(input('Digite o valor do primeiro número: '))
b = int(input('Digite o valor do segundo número: '))

print(f'Total da soma = {soma_numeros(numero1=a, numero2=b)}')
