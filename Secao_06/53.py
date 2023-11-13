

numero = int(input('Digite um inteiro positivo: '))

numero_impresso = 0

# Qtd de linhas impressas.
for i in range(1, numero + 1):

    qtd_numeros_a_imprimir_por_linha = i

# Qtd de números a imprimir por linha.
    while qtd_numeros_a_imprimir_por_linha > 0:

        numero_impresso += 1

        print(numero_impresso, end=' ')

        qtd_numeros_a_imprimir_por_linha -= 1
    
    print('\n')

