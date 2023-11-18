
A = []

while len(A) < 6:
    num = int(input('Digite um número par: '))

    if num % 2 == 0:
        A.append(num)


print(f'\nLista normal: {A}')
print(f'Lista inversa: {A[::-1]}')