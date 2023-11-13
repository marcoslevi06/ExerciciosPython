

valor_saque = float(input('Valor à sacar [R$]: '))
qtd_notas = 0

while valor_saque >= 0:

    while valor_saque % 100 == 0:
        valor_saque -= 100
        qtd_notas += 1
    
    