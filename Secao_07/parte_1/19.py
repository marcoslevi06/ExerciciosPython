

A = []

for i in range(50):
    valor = (i + 5 * i) % (i + 1)
    A.append(valor)

for i, valor in enumerate(A):
    print(f'Posição {i + 1}: {valor}')
