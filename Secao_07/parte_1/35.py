import random

a = b = 0
temp = 0
va = []
vb = []
vc = []

while True:
    a = int(input('Digite um (número a) entre 1 e 10.000: '))
    b = int(input('Digite um (número b) entre 1 e 10.000: '))
    if (1 > a < 10000) or (1 > b < 10000):
        a = input('Erro (número a). Digite um número entre 1 e 10.000: ')
        b = input('Erro (número b). Digite um número entre 1 e 10.000: ')
    else:
        break


# Adicionando cada algorismo como elemento na lista.
a = str(a)
b = str(b)

for elemento in a:
    va.append(int(elemento))

for elemento in b:
    vb.append(int(elemento))

print(va)
print(vb)

# Ordenando as listas

for i in range(0, len(va)):
    for j in range(0, len(va) - 1):
        if va[j] > va[j+1]:
            temp = va[j]
            va[j] = va[j+1]
            va[j+1] = temp

for i in range(0, len(vb)):
    for j in range(0, len(vb) - 1):
        if vb[j] > vb[j+1]:
            temp = vb[j]
            vb[j] = vb[j + 1]
            vb[j + 1] = temp


for i in range(0, len(va)):
    vc.append(va[i] + vb[i])


print(f'Array va: {va}')
print(f'Array vb: {vb}')
print(f'Array vc: {vc}')
