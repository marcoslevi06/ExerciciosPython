

x = int(input('Digite o valor de X: '))
y = int(input('Digite o valor de Y: '))
z = int(input('Digite o valor de Z: '))


opcao = int(input(
    'ESCOLHA QUAL DESEJA CALCULAR:\n[1] = Média Geométrica\ n[2Média Ponderada] \n[3]Média Harmônica \n[4]Aritmética \nR='))

if opcao == 1:
    print(f'Média Geométrica = { (x * y * z) ** (1/3) }')
elif opcao == 2:
    print(f'Média Ponderada = { ((x + 2) * (y + 3) * z) / 6 }')
elif opcao == 3:
    print(f'Média Harmônica = { 1 / ( (1/x) + (1/y) + (1/z) ) }')
elif opcao == 4:
    print(f'Média Aritimética: { (x + y + z) / 3 }')
else:
    print('Opção inválida.')
