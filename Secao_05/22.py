

idade = int(input('Digite sua idade: '))
tempo_de_servico = int(input('Digite a quantidade de tempo de trabalho: '))

if idade >= 65 or tempo_de_servico >= 30 or (idade >= 60 and tempo_de_servico >= 25):
    print('Você pode se aposentar.')
else:
    print('Você não pode se aposentar.')
