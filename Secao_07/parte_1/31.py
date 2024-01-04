

import random

A = []
B = []
C = []

for i in range(0, 10):
    A.append(random.randint(1, 100))
    B.append(random.randint(1, 100))

    if A[i] not in C:
        C.append(A[i])

    if B[i] not in C:
        C.append(B[i])


print(sorted(A))
print(sorted(B))
print(sorted(C))