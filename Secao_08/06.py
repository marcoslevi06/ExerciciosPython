
def converte_para_segundos(horas, minutos, segundos):

    total_segundos = (horas * 3600) + (minutos * 60) + segundos

    return total_segundos


valor_um = int(input('Informe o total de horas a serem convertidas: '))
valor_dois = int(input('Informe o total de minutos a serem convertidos: '))
valor_tres = int(input('Informe a quantidade de segundos que dejesa considerar: '))

print(f'Total de segundos = {converte_para_segundos(horas=valor_um, minutos=valor_dois, segundos=valor_tres)}')