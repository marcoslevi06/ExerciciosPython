
def calcula_volume(altura, raio):

    V = 3.14 * (raio**2) * altura

    return V

a = float(input('Digite o valor da altura: ')) 
b = float(input('Digite o valor do raio: '))

print(calcula_volume(a, b))