
import math

print(' **** CALCULANDO AS RAÍZES DE UMA EQUAÇÂO DO SEGUNDO GRAU *** \n')

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

if a != 0:
    delta = (b**2) - (4 * a * c)
    if delta < 0:
        print(f'Não existe raiz real. Delta = {delta:.2f}')
    elif delta == 0:
        raiz = -b / (2 * a)
    else:
        raiz_1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz_2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'Raiz 1 = {raiz_1:.2f}\nRaiz 2 = {raiz_2:.2f}')
else:
    print('Não é uma equação de segundo grau. (A deve ser diferente de zero.)')
