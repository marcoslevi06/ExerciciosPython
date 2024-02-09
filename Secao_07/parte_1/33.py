import random

# v = [0, 1, 2, 0]
v = []
temp = 0

for _ in range(0, 15):
    v.append(random.randint(0, 5))

print(v)

for i in range(0, len(v)):
    if v[i] == 0:
        for j in range(i, len(v) - 1):
            # temp = v[j+1]
            # v[j +1] = v[i]
            # v[i] = temp
            v[j], v[j + 1] = v[j + 1], v[j]

print("Resultado final da lista:", v)
