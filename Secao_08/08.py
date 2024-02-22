
def calcula_hipotenusa(cateto_oposto, cateto_adjacente):

    hipotenusa = (cateto_oposto**2 + cateto_adjacente**2) ** 0.5

    return hipotenusa

a = int(input('Digite o valor do cateto oposto: '))
b = int(input('Digite o valor do cateto adjacente: '))

print(calcula_hipotenusa(cateto_adjacente=b, cateto_oposto=a))