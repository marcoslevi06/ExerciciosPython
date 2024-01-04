

import random

A = []
B = []
C = []

for _ in range(0, 10):
    A.append(random.randint(1, 10))
    B.append(random.randint(1, 10))


for i in A:
    if (i in B) and (i not in C):
        C.append(i)


print(A)
print(B)
print(C)