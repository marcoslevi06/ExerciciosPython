
soma = 0

for i in range(1, 11):
    numero = int(input(f'Digite {i}º número: '))
    soma += numero

print(f'Média dos números = {soma/10:.2f}')