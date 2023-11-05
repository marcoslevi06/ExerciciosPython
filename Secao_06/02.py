
print('Usando For: ')
for i in range(1, 101):
    print(f'{i}')


print('\nUsando While')
cont = 0
while cont < 100:
    print(f'{cont + 1}')
    cont += 1

print('\nUsando Do While')

cont_do_while = 0
while True:
    print(cont_do_while + 1)
    cont_do_while += 1

    if cont_do_while == 100:
        break
