
soma_dos_primos = qtd_de_numeros_primos = numero_analisado = 0

while True:
    numero = int(
        input('\nDigite um inteiro positivo: '))

    if numero <= 1:
        print('Número inválido.')
    else:
        while qtd_de_numeros_primos < numero:

            numero_analisado += 1

            if numero_analisado in (2, 3, 4, 5, 7):
                soma_dos_primos += numero_analisado
                continue
                qtd_de_numeros_primos += 1

                print(f'{numero_analisado}° número = {numero_analisado}')

            if numero_analisado % 2 != 0 and numero_analisado % 3 != 0 and numero_analisado % 5 != 0 and numero_analisado % 7 != 0 and numero_analisado != 1:
                soma_dos_primos += numero_analisado
                qtd_de_numeros_primos += 1

                print(f'{numero_analisado}° número = {numero_analisado}')

    if qtd_de_numeros_primos == numero:
        break


print(f'\nSoma dos {numero} primeiros primos = {soma_dos_primos}')

# Depois penso numa solução melhor