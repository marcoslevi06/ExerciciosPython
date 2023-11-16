
n = int(input('Digite um número inteiro e positivo que represente a quantidade de múltiplos que deseja mostrar: '))

i = int(input('Digite um número inteiro e positivo [i]: '))

j = int(input('Digite um número inteiro e positivo [j]: '))

lista = list()
lista_ordenada = []

if n > 0:
    for x in range(0, n):

        multiplo_i = i * x
        multiplo_j = j * x

        lista.append(multiplo_i)
        lista.append(multiplo_j)

        # print(f'\n{x + 1}º múltiplo de {i} = {multiplo_i}')
        # print(f'{x + 1}º múltiplo de {j} = {multiplo_j}')
        # print(f'\n{lista}')
else:
    print('Número inválido.')


for y in lista:
    if y not in lista_ordenada:
        lista_ordenada.append(y)

print(f'\n{sorted(lista_ordenada[0:n-1])}')
