
import random

A = []
B = []
C = []

for _ in range(0, 10):
    A.append(random.randint(1, 20))
    B.append(random.randint(1, 20))


for elementoB in B:
    if elementoB not in A and elementoB not in C:
        C.append(elementoB)
print(A)
print(B)
print(C)
    


# OU

D = set()
E = set()
F = set()

for _ in range(0, 10):
    D.add(random.randint(1, 20))
    E.add(random.randint(1, 20))

print()
print(D)
print(E)
F = D - E
print(f'F = {F}')