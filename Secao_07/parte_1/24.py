import random

alunos = []

maior_aluno = menor_aluno = None

for i in range(0, 10):
    # utilizarei para salvar os dados daquele aluno no conjunto principal
    aluno_variavel = []

    numero = i + 1
    # determinando a altura entre 1m e 2m
    altura = round(random.uniform(1, 2), 2)

    aluno_variavel.append(numero)
    aluno_variavel.append(altura)

    alunos.append(aluno_variavel)


for i in alunos:
    print(f'Número do Aluno: {i[0]}         Altura do Aluno: {i[1]}')

    if maior_aluno is None or i[1] > maior_aluno[1]:
        maior_aluno = i

    if menor_aluno is None or i[1] < menor_aluno[1]:
        menor_aluno = i


print(f'\nMaior aluno:  Número = {maior_aluno[0]}      Altura = {maior_aluno[1]}')
print(f'\nMenor aluno:  Número = {menor_aluno[0]}      Altura = {menor_aluno[1]}')
