
numero_harmonico = 0
numero = int(input('Digite um número: '))


for i in range(1, numero + 1):
    numero_harmonico += 1/i
    print(f'--> 1/{i}')

print(f'\nH(n) = {numero_harmonico:.2f}')
