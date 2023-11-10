
maior = mais_lido = cont = 0
qtd_numeros = int(input('Quantos números deseja que sejam lidos? '))

for i in range(1, qtd_numeros + 1):
    numero = int(input(f'Digite {i}º número: '))

    # Verico se o numero digitado, é igual ao maior valor, para contar quantas vezes ele foi lido.
    if numero == maior:
        cont += 1

    # Aqui, verifico se houve mudança para um novo número maior, pra poder reiniciar a contagem de quantas vezes ele foi lido.
    if numero > maior:
        cont = 0

    # Verifico aqui se o novo numero digitado é maior que o valor atual.
    if maior == 0 or numero > maior:
        maior = numero
        cont += 1

# Contador serve para ver quantas vezes o maior valor foi lido
mais_lido = cont

print(f'\nO maior valor foi: {maior}.')
print(f'O {maior} foi lido {mais_lido} vez(es).')


# Dividir o problema em partes. Primeiro, descobrir o maior. Segundo, contar quantas vezes ele aparece. Terceiro, reinicar uma nova contagem quando houver um novo valor maior.