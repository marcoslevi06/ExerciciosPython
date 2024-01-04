import random

v = []
v1 = []
v2 = []

for i in range(0, 10):
    v.append(random.randint(1, 100))

    if v[i] % 2 != 0:
        v1.append(v[i])
    else:
        v2.append(v[i])


print(f'\nVetor V = {v}')
print(f'v1 = {v1}')
print(f'v2 = {v2}')