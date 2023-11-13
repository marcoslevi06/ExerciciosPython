
cont = 0

print(
    'DIGITE NÚMEROS PARA OBTER QUADRADO, CUBO E RAIZ QUADRADA. [PARA ENCERRAR DIGITE UM VALOR NEGATIVO OU ZERO].')

while True:
    cont += 1

    numero = int(input(f'\n{cont}° valor: '))

    if numero == 0 or numero < 0:
        print('FIM.')
        break

    print(
        f' ---> Quadrado = {numero**2}\n ---> Cubo = {numero**3}\n ---> Raiz Quadrada = {(numero**1/2):.2f}')
