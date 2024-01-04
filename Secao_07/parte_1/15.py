

A = []
B = []

for i in range(0, 20):

    num = int(input(f'Digite {i + 1}º número: '))

    B.append(num)

    if num not in A:
        A.append(num)

print(f'Lista sem números repetidos: {A}')
print(f'Lista com todos os números: {B}')
   