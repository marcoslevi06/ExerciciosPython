
def printa_triangulo(valor):

    num = (2 * valor) - 1
    cont = 0
    condicao_largura = False

    for i in range(0, num):

        if cont == valor:
            condicao_largura = True

        if condicao_largura is False:
            cont += 1
        
        if condicao_largura is True:
            cont -= 1
            
        print('*' * cont)

printa_triangulo(10)