
# Não entendi bem a pergunta, mas interpretei como sendo para ler 10 números
# Armazenar eles num vetor. Depois, ler um número X.
# E baseado nesse vetor de 10 números, contar quais desses são múltiplos de X.

A = []
B = []
qtd = 0

for i in range(0, 10):
    A.append(int(input(f'{i + 1}°: ')))


x = int(input('\nDigite um número X para verificarmos quantos dos números do vetor são múltiplos de X: '))

for i in A:
    if (i % x == 0) and (i != 0):
        qtd += 1
        B.append(i)

print(f'\nLista dos múltiplos: {B}')
print(f'Quantidade de múltiplos: {qtd}')
