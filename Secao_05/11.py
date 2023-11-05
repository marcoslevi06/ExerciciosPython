
a = int(input('Digite um número inteiro maior que 0 e que tenha até 3 dígitos: '))

dig1 = a // 100
dig2 = (a // 100) % 10
dig3 = a % 10

if a < 0:
    print('Número inválido.')
else:
    print(f'soma dos dígitos = {dig1 + dig2 + dig3}')
