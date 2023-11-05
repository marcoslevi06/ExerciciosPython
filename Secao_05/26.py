
distancia_km = float(input('Informe a distância em KM: '))
qtd_litros = float(
    input('Informe a quantidade de Litros consumidos no seu percurso:  '))

consumo = distancia_km/qtd_litros

if consumo < 8:
    print('VENDA O CARRO!')
elif 8 <= consumo <= 14:
    print('ECONÔMICO! ')
else:
    print('SUPER ECONÔMICO! ')
