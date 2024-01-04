

A = []

for i in range(0, 9):
    num = int(input('Digite número: '))

    if num < 0:
        A.append(0)
    else:
        A.append(num)

print(f'Vetor final = {A}')
