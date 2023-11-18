
A = []

for i in range(0, 6):
    A.append(int(input(f'{i + 1}º número: ')))

print(f'\nLista normal: {A}')
print(f'Lista inversa: {A[::-1]}')
