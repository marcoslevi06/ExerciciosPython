

A = []
B = []

for i in range(0, 10):
    A.append(int(input(f'{i + 1}º número: ')))

    if A.count(A[i]) >= 2:
        # print(A[i])
        if A[i] not in B:
            B.append(A[i])


print(f'Lista completa = {A}')
print(f'Lista com os números que se repetiram pelo menos umas vez: {B}')
