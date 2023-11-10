

while True:
    r1 = float(input('\nDigite o valor de R1: '))
    r2 = float(input('Digite o valor de R2: '))

    try:
        R = (r1 * r2) / (r1 + r2)
        print(f'Resistência = {R:.2f}')
        if R == 0:
            print('FIM!')
            break
    except ZeroDivisionError:
        print('>>>>> Não é possível dividir por zero. Denominador precisa ser != 0')
        continue
