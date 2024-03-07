

def maior_fator_primo(numero):
    '''
        Enquanto o DIVIDENDO for != 1, significa que ainda há o que dividir.
        Se o DIVIDENDO por CONT for 0, então ele é um fator.
            - maior_fator passa a ser o valor de CONT naquele instante.
            - e o DIVIDENDO recebe num novo valor, ou seja, o resto da divisão anterior.
            - fatores.append() guarda todos os fatores em ordem crescente.
        Se o DIVIDENDO por CONT for diferente de 0, então não é um fator de divisão, assim, adiciona +1 ao cont, para verificar se o próximo número é.
    '''
    cont = 2
    dividendo = maior_fator = numero
    fatores = list()

    while dividendo != 1:

        if dividendo % cont == 0:
            maior_fator = cont
            dividendo /= cont
            fatores.append(maior_fator)
        else:
            cont += 1

    # retorna uma tupla com o maior valor e os fatores.
    return maior_fator, fatores


num = int(input('Digite um número: '))

print(f'Maior fator primo de {num} = {maior_fator_primo(num)}')
