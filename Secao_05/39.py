

salario_atual = float(input('Digite o salário atual: '))
tempo_servico = int(input('Digite o tempo de serviço: '))

valor_reajustado = 0

if salario_atual <= 500 and tempo_servico < 1:
    valor_reajustado = salario_atual * 1.25
elif salario_atual <= 1000 and tempo_servico <= 3:
    valor_reajustado = salario_atual * 1.20 + 100
elif salario_atual <= 1500 and tempo_servico <= 6:
    valor_reajustado = salario_atual * 1.15 + 200
elif salario_atual <= 2000 and tempo_servico <= 10:
    valor_reajustado = salario_atual * 1.10 + 300
elif salario_atual > 2000 and tempo_servico > 10:
    valor_reajustado = salario_atual

print(f'O valor após o reajuste é de R$ {valor_reajustado:.2f}')
