
soma_primos = 0

a = int(input("Digite primeiro valor: "))
b = int(input("Digite segundo valor: "))

if a > b:
    print("O primeiro valor deve ser menor que o segundo. Fim de programa.")
else:
    for i in range(a, b + 1):
        if i in (2, 3, 5, 7):
            soma_primos += i
            print(i)

        if (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0):
            soma_primos += i
            print(i)

    print(f'Quantidade de primos = {soma_primos}')
