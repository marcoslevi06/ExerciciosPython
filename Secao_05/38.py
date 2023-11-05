
data = input(
    'Informe sua data de nascimento no padrão dia/mês/ano. [Ex: 13/6/2000].\n R = ').split('/')


dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

# '''
# data:       1 3 / 6 / 2 0 0 0
# índice:     0 1 2 3 4 5 6 7 8
# '''

# print(dia)
# print(mes)
# print(ano)
# print(data)


# Verificando primeiro se é um mês válido.

if 1 <= ano <= 2023:
    if 1 <= mes <= 12:
        if mes == 2:  # Verificando se o mês de fereiro cai num ano bissexo e se é válido.
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if 1 <= dia <= 29:
                    print('Data válida.')
                else:
                    print('Data inválida.')
        # Verificando se o mês tem 30 dias pra Abril, Junho, Setembro e Novembro, como passado na questão.
        if mes in (4, 6, 9, 11):
            if 1 <= dia <= 30:
                print('Data válida.')
            else:
                print('Data inválida.')
        else:
            if 1 <= dia <= 31:
                print('Data válida.')
            else:
                print('Data inválida.')
    else:
        print('Data inválida.')
else:
    print('Data inválida.')
