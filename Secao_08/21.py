
def conta_primos(numero):

    num = numero
    qtd = 0
    lista_primos = list()

    while num > 0:
        
        if (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0) or (num % 7 == 0) or (num == 1):
            valor = False
        else:
            valor = True

        if num in (2, 3, 5, 7):
            valor = True

        if valor is True:
            qtd += 1
            lista_primos.append(num)

        print(num)
        num -= 1

    return f'Quantidade números primos até {numero} = {qtd}. Lista dos primos: {lista_primos}'


print(conta_primos(100))