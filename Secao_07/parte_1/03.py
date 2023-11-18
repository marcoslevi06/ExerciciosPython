
A = []
B = []

for i in range(0, 10):
    A.append(float(input(f'{i + 1}° valor: ')))
    B.append(A[i]**2)

print(f'\nLista A = {A}')
print(f'Lista B = {B}')
