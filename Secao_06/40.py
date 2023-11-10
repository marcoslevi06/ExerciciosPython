
maior = menor = 0

while True:
    numero = int(
        input('Digite um número [para encerrar digite um número negativo]: '))

    if maior == 0 or numero > maior:
        maior = numero

    if menor == 0 or numero < menor:
        menor = numero

    if numero < 0:
        print('Fim.')
        break


print(
    f'\nO maior número digitado = {maior}\nO menor número digitado = {menor}')


# Dica: lembrar de inicializar a variável de comparação com NONE ao invés de 0.