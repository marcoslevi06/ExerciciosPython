

while True:

    opcao = int(
        input('\n[1] - Para converter km/h ---> m/s.\n[2] - Para converter m/s ---> km/h\n[3] Finalizar. R = '))

    if opcao == 1:

        km = float(input('\nInfome a quantidade de km/h a ser convertido: '))

        if km >= 0:
            print(f'{(km/3.6):.2f} m/s')
        else:
            print('Valor inválido.')
            break

    elif opcao == 2:

        m = float(input('\nInfome a quantidade de m/s a ser convertido: '))

        if m >= 0:
            print(f'{(m * 3.6):.2f} km/h')
        else:
            print('Valor inválido.')
            break

    elif opcao == 3:
        print('\nFIM!')
        break
   