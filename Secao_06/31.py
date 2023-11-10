
S = denominador = 0

# for i in range(1, 100):
#     if i % 2 != 0:
#         denominador += 1
#         S += i/denominador

# ou

for i in range(1, 100, 2):
    denominador += 1
    S += i/denominador

print(f'{S:.2f}')
