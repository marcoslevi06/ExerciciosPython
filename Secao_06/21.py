
soma_dos_pares = 0
multiplicacao_impares = 1

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1 == numero2:
    maior = menor = numero1
elif numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1


for i in range(menor, maior + 1):
    if i % 2 == 0:
        soma_dos_pares += i
    else:
        multiplicacao_impares *= i
