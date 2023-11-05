

salario = float(input('Digite o salário: '))
valor_prestacao = float(input('Digite o valor da prestação: '))

if valor_prestacao > (salario * 0.2):
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
