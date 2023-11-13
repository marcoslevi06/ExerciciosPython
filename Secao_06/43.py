
soma_idade = cont = 0

while True:
    idade = int(input('Digite sua idade [digite 0 para encerrar]: '))

    if idade != 0:
        soma_idade += idade
        cont += 1
    else:
        try:
            print(f'\nMédia de idades = {soma_idade/cont:.2f}')
            print('FIM.')
            break
        except ZeroDivisionError:
            print('Nenhuma pessoa foi informada.')
            break