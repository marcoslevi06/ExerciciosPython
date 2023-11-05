
numero = int(input('Digite um número: '))

for i in range(0, numero + 1):
    print(i)


# usando While

numero = int(input('Digite um número: '))

cont = 0
while numero > -1:
    print(cont)
    cont += 1
    numero -= 1
