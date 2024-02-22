
def calcula_economia(km, litros):
    consumo = km/litros

    if consumo > 8:
        R = 'Venda o carro!'
    elif 8 <= consumo <= 14:
        R = 'Econômico!'
    elif consumo > 12:
        R = 'Super Econômico!'

    return R


distancia_percorrida = float(input('Informe a distância percorrida [km]: '))
litros = float(input('Informe a quantidade de litros consumidos: '))

print(calcula_economia(km=distancia_percorrida, litros=litros))