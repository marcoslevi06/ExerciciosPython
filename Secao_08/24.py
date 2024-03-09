
def gera_triangulo(valor):

    altura = valor
    cont = 0
    cont_margem = valor
    margem = 0

    for i in range(0, altura):
        
        cont_margem -= 1
        margem = ' ' * cont_margem

        cont += 1
        
        print(margem, '*' * ( 2 * cont - 1) )


gera_triangulo(6)