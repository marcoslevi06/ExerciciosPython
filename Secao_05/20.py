
a = float(input('Digite o primeiro lado do triangulo: '))
b = float(input('Digite o segundo lado do triangulo: '))
c = float(input('Digite o terceiro lado do triangulo: '))

if a < b + c and b < a + c and c < a + b:
    print('Os lados informados podem formar um triangulo.')
    if a == b == c:
        print('Triangulo equilátero.')
    elif a == b or a == c or b == c:
        print('Triangulo isósceles.')
    else:
        print('Triangulo escaleno.')
