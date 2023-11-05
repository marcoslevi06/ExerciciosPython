
altura = float(input('Digite o sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))


if altura < 1.20:
    if peso < 60:
        print('Classificação A.')
    elif 60 <= peso <= 90:
        print('Classificação D.')
    else:
        print('Classificação G.')
elif 1.20 <= altura <= 1.70:
    if peso < 60:
        print('Classificação B.')
    elif 60 <= peso <= 90:
        print('Classificação E.')
    else:
        print('Classificação F.')
else:
    if peso < 60:
        print('Classificação G.')
    elif 60 <= peso <= 90:
        print('Classificação H.')
    else:
        print('Classificação I.')
