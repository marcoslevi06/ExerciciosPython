
A = []

for i in range(0, 5):
    A.append(int(input(f'{i + 1}º número: ')))

while True:

    opcao = int(input('\n[1] Para mostrar o vetor na ordem informada.\n[2] Para mostrar o vetor na ordem inversa.\nR: '))
        
    if opcao == 0:
        ('FIM')
        break
    elif opcao == 1:
        print(A)
        break
    elif opcao == 2:
        print(A[::-1])
        break
    else:
        print('Inválido.')