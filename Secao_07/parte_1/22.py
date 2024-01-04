import random

A = []
B = [] 
C = []

for i in range(0, 10):
    A.append(random.randint(1, 10))
    B.append(random.randint(1, 10))
    
    C.append(A[i])
    C.append(B[i])

print(f'lista que deve aparcer com a posição PAR = {A}')
print(f'lista que deve aparecer com a posição ÍMPAR = {B}')

# Obs considerei 0 como parte dos pares,

for indice, valor in enumerate(C):
    print(f'{indice}    ---->  {valor}')