

print('*** MENU ***')
print('Cachorro Quente [100] \nBauro Simples [101] \nBauro com Ovo [102] \nHamburguer [103] \nCheeseburguer [104] \nSuco [105] \nRefrigerante [106]')

codigo = int(input('\nDigite o código: '))
quantidade = int(input('O quanto deseja consumir? '))

if codigo == 100:
    print(f'O valor a ser pago no Cachorro Quente é: R$ {1.20 * quantidade}')
elif codigo == 101:
    print(f'O valor a ser pago no Bauro Simples é: R$ {1.30 * quantidade}')
elif codigo == 102:
    print(f'O valor a ser pago no Bauro com Ovo é: R$ {1.50 * quantidade}')
elif codigo == 103:
    print(f'O valor a ser pago no Hamburguer é: R$ {1.20 * quantidade}')
elif codigo == 104:
    print(f'O valor a ser pago no Cheeseburguer é: R$ {1.70 * quantidade}')
elif codigo == 105:
    print(f'O valor a ser pago no Suco é: R$ {2.20 * quantidade}')
elif codigo == 106:
    print(f'O valor a ser pago no Refrigerante é: R$ {1.00 * quantidade}')
else:
    print('Código inválido!')
