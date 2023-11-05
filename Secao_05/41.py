

peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em M: '))

imc = peso / altura ** 2

if imc < 18.5:
    print(f'IMC: {imc:.2f} - Abaixo do peso')
elif imc < 25:
    print(f'IMC: {imc:.2f} - Saudável')
elif imc < 30:
    print(f'IMC: {imc:.2f} - Peso em Excesso')
elif imc < 35:
    print(f'IMC: {imc:.2f} - Obesidade Grau I')
elif imc < 40:
    print(f'IMC: {imc:.2f} - Obesidade Grau II')
else:
    print(f'IMC: {imc:.2f} - Obesidade Grau III (obesidade Mórbida)')
