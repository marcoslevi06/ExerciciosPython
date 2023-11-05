
opcao = int(input(
    'Escolha uma opção:\n [1] Soma de dois números.\n [2] Diferença entre dois números.\n [3] Produto entre dois números.\n [4] Divisão entre dois números.\n R = '))

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
