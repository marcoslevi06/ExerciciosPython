
maior = menor = None

for i in range(1, 11):
    numero = int(input(f'{i}° número: '))

    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
