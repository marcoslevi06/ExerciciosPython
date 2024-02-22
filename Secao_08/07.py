
def converte_graus(celsius):

    F = celsius * (9.0/5.0) + 32

    return F


n = int(input('Digite a quantidade de graus Celsius que deseja converter para Fahrenheit: '))

print(converte_graus(n))