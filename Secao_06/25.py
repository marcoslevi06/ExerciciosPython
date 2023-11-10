
soma_dos_multiplos_3_e_5 = 0

for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        soma_dos_multiplos_3_e_5 += i

print(f'Soma dos múltiplos de 3 ou 5 de 1 a 1000: {soma_dos_multiplos_3_e_5}')
