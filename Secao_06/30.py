
sequencia1 = sequencia2 = sequencia3 = 0

n = int(input('Digite um número: '))

for i in range(1, n + 1):
    sequencia1 += n

print(sequencia1)


for i in range(1, n + 1):
    if i % 2 == 0:
        sequencia2 -= i
    else:
        sequencia2 += i

print(sequencia2)


for i in range(1, n + 1):
    if i % 2 != 0:
        sequencia3 += i

print(sequencia3)