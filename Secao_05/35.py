
data = input('Informe uma data de acordo com o padrão dd/mm/yyyy: ')

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

if 1 <= mes <= 12:
    if 1 <= ano <= 9999:
        if mes == 2:
            if 1 <= dia <= 28:
                print('Data válida')
            elif dia == 29:
                if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                    print('Data válida')
                else:
                    print('Data inválida')
            else:
                print('Data inválida')
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if 1 <= dia <= 30:
                print('Data válida')
            else:
                print('Data inválida')
        else:
            if 1 <= dia <= 31:
                print('Data válida')
            else:
                print('Data inválida')
    else:
        print('Data inválida. O ano deve estar entre 1 e 9999')
else:
    print('Data inválida. O mês deve estar entre 1 e 12')
