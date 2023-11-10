
S = cont = 0

for i in range(1, 6):
    cont += 2
    denominador = cont
    while denominador > 0:
        S += i/denominador
        denominador -= 1

print(f'S = {S:.2f}')
