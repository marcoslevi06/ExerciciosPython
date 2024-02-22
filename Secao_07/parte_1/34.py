import random

# v = [0, 1, 2, 0]
v = []

cont = 0

while len(v) < 10:
    a = random.randint(0, 10)
    if a not in v: 
        v.append(a)

print(v)
