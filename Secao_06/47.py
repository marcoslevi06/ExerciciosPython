
soma = divisao = multiplicacao = subtracao = 0

while True:
    opcao = int(input(
        '\n[1] Adição: \n[2] Subtração: \n[3] Multiplicação: \n[4] Divisão: \n[5]Saída: '))

    if opcao == 1:
        qtd = int(input('Quantos números deseja somar? '))

        for i in range(1, qtd + 1):
            numero = int(input(f'{i}º número: '))

            soma += numero

        print(f'Soma = {soma}')

    elif opcao == 2:
        qtd = int(input('Quantos números deseja subtrair? '))

        for i in range(1, qtd + 1):
            numero = int(input(f'{i}º número: '))

            subtracao -= numero

        print(f'Subtração = {subtracao}')

    elif opcao == 3:
        qtd = int(input('Quantos números deseja multiplicar? '))

        for i in range(1, qtd + 1):
            numero = int(input(f'{i}º número: '))

            multiplicacao *= numero

        print(f'Multiplicação = {multiplicacao}')

    elif opcao == 4:
        numerador = int(input('Digite numerador: '))
        denominador = int(input('Digite denominador diferente de zero: '))
        if denominador != 0:
            divisao = numerador / denominador
            print(f'Divisão = {divisao:.2f}')
        else:
            print('Denominador não pode ser zero.')

    elif opcao == 5:
        print('\nFIM.')
        break
