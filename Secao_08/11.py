
def calcula_media(nota1, nota2, nota3, tipo_media):
    ''' Informe A para calcular a média aritmética.
        Informe P para calcular a média ponderada.    
    '''

    if tipo_media == 'A':
        media = (nota1+nota2 + nota3)/3
    elif tipo_media == 'P':
        media = ((nota1*5) + (nota2*3) + (nota3*2)) / 10
    else:
        media = 'VALOR INVÁLIDO.'

    return media


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
tipo = input(
    'Digite [A] para Calcular média Aritimética. Digite [P] para calcular a média ponderada.')


resultado = calcula_media(n1, n2, n3, tipo)
print(f'Média: {resultado}')
