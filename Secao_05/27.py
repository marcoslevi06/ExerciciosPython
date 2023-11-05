

idade_nadador = int(input('Informe sua idade: '))

if 5 >= idade_nadador <= 7:
    print('Infantil A.')
elif 8 >= idade_nadador <= 10:
    print(f'Infantil B.')
elif 11 >= idade_nadador <= 13:
    print(f'Juvenil A.')
elif 14 >= idade_nadador <= 17:
    print(f'Juvenil B.')
else:
    print('Sênior.')
