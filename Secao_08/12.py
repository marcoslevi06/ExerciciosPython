


def soma_algarismos(numero):

    if numero > 0:
        soma = 0
        num = str(numero)

        for algarismos in num:
            soma += int(algarismos)
    else:
        soma = 'Número inválido.'

    return soma

n = int(input('Digite um número: '))

print(soma_algarismos(n))