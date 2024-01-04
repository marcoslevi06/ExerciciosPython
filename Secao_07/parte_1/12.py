

A = []

for i in range(0, 5):
    A.append(float(int(input(f'{i + 1}°: '))))

print(f'\nLista completa = {A}')
print(f'Maior = {max(A)}    Menor = {min(A)}    Média = {sum(A)/len(A):.2f}')
