
soma_dos_pares = anterior = atual = numero_fibonacci = 0

while numero_fibonacci < 4000000000:

    print(f' --->   {numero_fibonacci}')

    # Inicianiza a contagem após o zero
    if numero_fibonacci == 0:
        atual = 1

    anterior, atual = atual, numero_fibonacci

    numero_fibonacci = anterior + atual

    if numero_fibonacci % 2 == 0:
        soma_dos_pares += numero_fibonacci

print(
    f'\nSoma dos pares da sequência de Fiboacci até 4.000.000.000: {soma_dos_pares}')
