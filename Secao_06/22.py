
cont = soma_notas = 0

while True:
    nota = float(input('Digite a nota da 10 à 20: '))

    if 10 <= nota <= 20:
        soma_notas += nota
        cont += 1
    else:
        print('Nota inválida. Fim de programa.')
        
        if cont > 0:
            print(f'A sua média com as notas fornecidas foi: {soma_notas/cont:.2f}')
        else:
            print('E não foi possível calcular sua média, não há notas válidas.')
        break
