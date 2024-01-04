
import random

A = []
B = [] 
produto_escalar = 0

for i in range(0, 5):
    A.append(round(random.uniform(1, 10), 2))
    B.append(round(random.uniform(1, 10), 2))

    produto_escalar += A[i] * B[i]

print(A)
print(B)
print(produto_escalar)