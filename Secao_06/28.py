
E = 0
numero = int(input('Digite um número inteiro positivo: '))

if numero > 0:
    for i in range(1, numero + 1):
        while i > 0:
            E += 1/i
            i -= 1
else:
    print('Número inválido.')

print(f'E = {E:.2f}')
