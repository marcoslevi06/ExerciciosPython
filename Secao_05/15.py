# Como não existe switch-case em Python, usei um if-elif-else para resolver a questão.


num = int(input('Digite um número inteiro de um 1 à 7: '))

if num == 1:
    print('Domingo')
elif num == 2:
    print('Segunda-feira')
elif num == 3:
    print('Terça-feira')
elif num == 4:
    print('Quarta-feira')
elif num == 5:
    print('Quinta-feira')
elif num == 6:
    print('Sexta-feira')
elif num == 7:
    print('Sábado')
else:
    print('Número inválido.')
