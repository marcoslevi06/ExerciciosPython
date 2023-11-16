
soma_primos = 0

for i in range(1, 100):

    if i in(2, 3, 5, 7):
        soma_primos += i
        print(i)

    if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0):
        soma_primos += i
        print(i)
    
print(f'Soma dos primos = {soma_primos}')
