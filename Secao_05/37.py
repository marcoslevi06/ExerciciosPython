
print(
    'Digite a hora de chegada e saída de acordo com o padrão hora:minuto. [Ex: 12:00]')

chegada = input('\nEntrada: ').replace(':', '.')
saida = input('\nSaída:  ').replace(':', '.')

dif_horas = (float(saida[0:2]) - float(chegada[0:2]))
dif_minutos = (float(saida[3:5]) - float(chegada[3:5]))

# Tratando a diferença de horas de um dia à outro.
if saida[0:2] <= chegada[0:2] and saida[3:5] < chegada[3:5]:
    dif_horas = 24 + dif_horas

# Tratando a diferença de minutos de um dia à outro.
if saida[3:5] < chegada[3:5]:
    dif_minutos = 60 + dif_minutos
    dif_horas -= 1

total_minutos = (dif_horas * 60) + dif_minutos

# Verificando a taxa para 1 e 2 horas.
if total_minutos <= 120:
    if total_minutos <= 60:
        print('Total a pagar: R$ 1,00')
    else:
        print(f'Total a pagar: R$ {(total_minutos // 60 + 1) * 1}')
# Verificando a taxa para 3 e 4 horas.
elif total_minutos <= 240:
    if total_minutos < 180:
        print(f'Total a pagar: R$ { (total_minutos // 60 + 1) * 1.4}')
    elif total_minutos == 180:
        print(f'Total a pagar: R$ { (total_minutos // 60) * 1.4}')
    else:
        print(f'Total a pagar: R$ { (total_minutos // 60 + 1) * 1.4}')
# Verificando a taxa para horários maiores que 5 horas.
else:
    qtd_horas = total_minutos // 60 + 1
    print(f'Total a pagar: R$ {qtd_horas * 2}')


# print(f'Dif Horas = {dif_horas}')
# print(f'Dif Minutos = {dif_minutos}')
# print(f'Total Minutos = {total_minutos}')

print(
    f'Tempo total no estacionamento: {dif_horas} horas e {dif_minutos} minutos.')
