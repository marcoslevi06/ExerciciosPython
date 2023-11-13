

# joao recere x/3 de carlos

qtd_mes = 1

salario_carlos = 1

salario_joao = 1/3

while salario_carlos >= salario_joao:

    salario_carlos += salario_carlos * 0.002
    salario_joao += salario_joao * 0.005

    qtd_mes += 1

    print(
        f'\n{qtd_mes}º:\nCarlos = {salario_carlos:.2f}\nJoão = {salario_joao:.2f}')
