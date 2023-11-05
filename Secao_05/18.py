
opcao = int(input(
    'Digite:\n [1] - Adição\n [2] - Subtração\n [3] - Multiplicação\n [4] - Divisão:\n R = '))

if opcao == 1:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print(f'{num1} + {num2} = {num1 + num2}')
elif opcao == 2:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print(f'{num1} - {num2} = {num1 - num2}')
elif opcao == 3:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print(f'{num1} * {num2} = {num1 * num2}')
elif opcao == 4:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print(f'{num1} / {num2} = {num1 / num2}')
else:
    print('Opção inválida.')
