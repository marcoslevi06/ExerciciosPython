
mg = 1.07
sp = 1.12
rj = 1.15
ms = 1.08


valor = float(input('Digite o valor do produto R$: '))
destino = input(
    'Digite a siglha do estado de destino: \n[MG] \n[SP] \n[RJ] \n[MS] \nR= ').lower()

if destino == 'mg':
    print(f'Valor final = {valor * mg:.2f}')
elif destino == 'sp':
    print(f'Valor final = {valor * sp:.2f}')
elif destino == 'rj':
    print(f'Valor final = {valor * rj:.2f}')
elif destino == 'ms':
    print(f'Valor final = {valor * ms:.2f}')
else:
    print('Valor inválido.')
