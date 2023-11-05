
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if nota1 >= 0 and nota1 <= 10:
    if nota2 >= 0 and nota2 <= 10:
        media = (nota1 + nota2) / 2
        print(f'A média é {media}')
    else:
        print('Nota inválida. Fim de programa.')
else:
    print('Nota inválida. Fim de programa.')
