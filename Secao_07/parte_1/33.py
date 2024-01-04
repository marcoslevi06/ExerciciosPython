import random

v = []

for i in range(0, 15):
    v.append(random.randint(0, 10))

print(v)
print(sorted(v))

for i in v:
    for j in range(0, len(v)):

        if i <= v[j]:
            v[j] = i
            pos2 = v[j]+ 1


            v[pos1] = v[j]
            break

print(v)
