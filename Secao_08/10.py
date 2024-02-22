

def qual_maior(numero1, numero2):
    
    if numero1 > numero2:
        maior = numero1
    elif numero1 == numero2:
        maior = 'Números são iguais.'
    else:
        maior = numero2

    return maior


a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

print(qual_maior(a, b))