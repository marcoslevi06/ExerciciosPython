

def medida_triangulo(valor1, valor2, valor3):

    if valor1 < (valor2 + valor3) and valor2 < (valor1 + valor3) and valor3 < (valor1 + valor2):

        if valor1 == valor2 == valor3:
            return 'É um triângulo. Do tipo Equilátero.'
        elif valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
            return 'É um triângulo. Do tipo Isóceles.'
        else:
            return 'É um triângulo. Do tipo Escaleno.'
    else:
        return 'Não é um triângulo.'


a = float(input('Digite o 1º valor: '))
b = float(input('Digite o 2º valor: '))
c = float(input('Digite o 3º valor: '))

print(medida_triangulo(a, b, c,))