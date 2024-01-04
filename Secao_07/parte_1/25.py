
A = []

cont = 0

while len(A) < 100:
    cont += 1

    if (cont % 7 == 0) or (cont % 10 == 7):
        A.append(cont)


for indice, valor in enumerate(A):
    print(f'{indice + 1}        {valor}')
