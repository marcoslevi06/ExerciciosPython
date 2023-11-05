numero = int(input("Digite um número: "))

if numero % 3 == 0 or numero % 5 == 0:
    print(f"{numero} é divisível por 3 ou 5.")
    if numero % 3 == 0:
        print(f"{numero} é divisível por 3.")
    else:
        print(f"{numero} é divisível por 5.")
