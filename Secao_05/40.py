

custo_fabrica = float(input('Digite o custo de fábrica do carro: '))
custo_consumidor = 0

if custo_fabrica <= 12000:
    custo_consumidor = custo_fabrica * 1.05
elif custo_fabrica <= 25000:
    custo_consumidor = custo_fabrica * 1.10 + 2000
elif custo_fabrica > 25000:
    custo_consumidor = custo_fabrica * 1.15 + 2500

print(f'O custo do consumidor é de R$ {custo_consumidor:.2f}')
