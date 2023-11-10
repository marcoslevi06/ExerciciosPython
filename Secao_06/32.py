import random

n = int(input('Quantas vezes quer jogar os dados? '))

for i in range(1, n + 1):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print(f'\n{i}ª Rodada: d1 = {d1} , d2 = {d2}')
    if d1 > d2:
        print(f'O primeiro dado[{d1}] é MAIOR que o segundo [{d2}].')
    elif d1 < d2:
        print(f'O primeiro dado[{d1}] é MENOR que o segundo [{d2}].')
    else:
        print(f'O primeiro dado[{d1}] é IGUAL que o segundo [{d2}].')
