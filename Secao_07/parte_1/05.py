

A = []

conte_par = 0

for i in range(0, 10):
    A.append(int(input(f'Posição {i + 1}:   ')))

    if A[i] % 2 == 0:
        conte_par += 1
        # print(A[i])


print(f'\nQuantidade de números pares digitados: {conte_par}')
