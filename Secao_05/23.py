
ano = int(input('Digite um ano para que possamos verificar se ele é bissexto: '))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print('Esse ano é bissexto.')
else:
    print('Esse ano não é bissexto.')
