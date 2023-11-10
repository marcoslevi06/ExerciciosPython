

while True:
    base = float(input('Digite a base exata de um triângulo: '))

    if base <= 0:
        base = float(input('Valor inválido. Digite uma base válida. '))
    else:
        altura = float(input('Digite a altura exata de um triângulo: '))
        if altura <= 0:
            altura = float(input('Valor inválido. Digite uma altura válida. '))
        else:
            area = (base * altura) / 2

    print(f'Área do Triângulo = {area}')
