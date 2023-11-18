


A = [1, 0, 5, -2, -5, 7]

soma_posicoes = A[0] + A[1] + A[5]

print(f'\nSoma das posiçõe A[0] + A[1] + A[5] = {soma_posicoes}   -   Vetor completo: {A}\n')

A[4] = 100

for indice ,elemento in enumerate(A):
    print(f'[{indice}]   -   {elemento}')