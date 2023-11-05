import math

num = int(input('Digite um número: '))

if num > 0:
    r = math.log(num)
    print(f'{r}')
else:
    print('Inválido.')
