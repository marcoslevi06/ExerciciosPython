
qtd_habitantes = int(input("Digite a quantidade de habitantes: "))

maior_consumo = 0
menor_consumo = 0
media_consumo = 0

for i in range(1, qtd_habitantes + 1):
    consumo = float(input(f"Digite o consumo kwh do {i}º habitante: "))
    codigo = int(input(f"Digite o código do {i}º habitante: "))

    if consumo > maior_consumo:
        maior_consumo = consumo
        maior_consumo_codigo = codigo

    if consumo < menor_consumo:
        menor_consumo = consumo
        menor_consumo_codigo = codigo

    media_consumo += consumo

media_consumo /= qtd_habitantes

print(
    f"\nO maior consumo foi de {maior_consumo} kwh, do habitante de código {maior_consumo_codigo}.")
print(
    f"O menor consumo foi de {menor_consumo} kwh, do habitante de código {menor_consumo_codigo}.")
print(f"A média de consumo foi de {media_consumo} kwh.")
