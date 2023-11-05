
soma = 0
cont = 0
for i in range(1, 11):
    numero = int(input('{i}° número: '))
    if numero > 0:
        cont += 1
        soma += numero

print(f'Média dos números positivos = {soma/cont:.2f}')
