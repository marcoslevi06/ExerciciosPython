from random import randint

qtd_tentativas = 0

numero_aleatorio = randint(1, 1000)
# print(numero_aleatorio)

while True:

    palpite = int(input('\nInforme seu palpite: '))
    qtd_tentativas += 1

    if palpite == numero_aleatorio:
        print(f'Parabéns, você acertou depois de {qtd_tentativas} tentativas!!!!')
        break
    elif palpite < numero_aleatorio:
        print('Seu palpite foi MENOR que o número secreto.')
    elif palpite > numero_aleatorio:
        print('Seu palpite foi MENOR que o número secreto.')
