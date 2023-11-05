
numero = int(input('Digite um número: '))

for i in range(0, numero + 1):
    print(numero - i)


# usando While

numero = int(input('Digite um número: '))
cont = 0

while cont <= numero:
    print(numero - cont)
    cont += 1
