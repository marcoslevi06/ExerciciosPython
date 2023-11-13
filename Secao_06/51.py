
salario = 2000
ano = 1995
aumento = 0

while ano <= 2023:

    if ano == 1996:
        aumento = salario * 0.15
    elif ano > 1996:
        aumento = aumento * 2

    salario = salario + aumento

    print(f'\nAno: {ano} Salário = {salario:.2f} Aumento = {aumento}')
    ano += 1
