
def verifica_numero(numero):

    # Fiz apenas para exercitar o operador ternário.
    # resultado = 1 if numero % 2 == 0 else (-1 if numero % 2 != 0 else 0)

    if numero != 0:
        if numero % 2 == 0:
            resultado = 1
        else:
            resultado = -1
    else:
        resultado = numero

    return resultado

num = int(input('Digite um número para verificar se ele é par ou ímpar: '))

print(verifica_numero(num))