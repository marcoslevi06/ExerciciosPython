
# cada termo subsequente é a soma dos dois anteriores

anterior = atual = numero_fibonacci = 0

while True:

    numero = int(input('Digite um número inteiro positivo: '))

    if numero < 0:
        numero = int(input('Número inválido. Digite um número positivo: '))

    for i in range(0, numero):

        numero_fibonacci = anterior + atual
        print(numero_fibonacci)

        if i == 1:
            atual = i

        anterior = atual
        atual = numero_fibonacci

        if numero_fibonacci > numero:
            print('\nFIM!')
            break
