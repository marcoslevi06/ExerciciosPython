from datetime import datetime

def converte_data(data_para_converter):
  
    data = datetime.strptime(data_para_converter, '%d/%m/%Y')

    data_extenso = data.strftime('%d de %B de %Y')

    return data_extenso


data = input('Digite uma data no formato: dd/mm/aaaa: ')

try:
    print(converte_data(data))
except ValueError:
    print('Formato iválido amigão. Depois tente novamente.')