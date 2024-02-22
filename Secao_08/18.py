
def calcula_expoente(numero, expoente):

    R = numero**expoente

    return R

x = float(input('Digite o valor para o número X: '))
z = float(input('Digite o valor para o expoente Z: '))

print(f'{x} elevado a {z} é igual a {calcula_expoente(x, z):.2f}')
