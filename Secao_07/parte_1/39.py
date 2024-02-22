

numero = int(input('Digite um número n: '))
cont = 0

for i in range(1 , numero + 1):
    cont += 1
    for j in range(1, cont + 1):
        print(i, end=' ')

    print()