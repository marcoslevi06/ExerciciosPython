
import random

x = []
y = []


while len(x) < 5:
    num = random.randint(1, 10)

    if num not in x:
        x.append(num)


while len(y) < 5:
    num = random.randint(1, 10)

    if num not in y:
        y.append(num)

print(x)
print(y)

soma = []
produto = []
diferenca = []
intersecao = []
uniao = []

for i in range(0, len(x)):
    soma.append(x[i] + y[i])
    produto.append(x[i] * y[i])

    if x[i] not in y:
        diferenca.append(x[i])

    if (x[i] in y) and (x[i] not in intersecao):
        intersecao.append(x[i])

    if x[i] not in uniao:
        uniao.append(x[i])

    if y[i] not in uniao:
        uniao.append(y[i])


print(f'\nSoma: {soma}')
print(f'Produto: {produto}')
print(f'Diferença X - Y:{diferenca}')
print(f'Interseção: {sorted(intersecao)}')
print(f'União: {sorted(uniao)}')
