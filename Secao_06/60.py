
soma_numeros = 0
qtd_numeros = 0
media_numeros = 0
maior_numero = menor_numero = None
media_pares = soma_pares = 0

while True:
    numero = int(input("Digite um número[-1 para finalizar.]: "))

    if numero == -1:
        break

    soma_numeros += numero
    qtd_numeros += 1

    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

    if menor_numero is None or numero < menor_numero:
        menor_numero = numero

    if numero % 2 == 0:
        soma_pares += numero


media_numeros = soma_numeros / qtd_numeros
media_pares = soma_pares / qtd_numeros

print(f"\nSoma dos números: {soma_numeros}")
print(f"Quantidade de números: {qtd_numeros}")
print(f"Média dos números: {media_numeros:.2f}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos pares: {media_pares:.2f}")
