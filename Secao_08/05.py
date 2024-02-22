

def volume_esfera(raio):

    volume = round((4/3) * 3.14 * (raio**3), 2)

    return volume

n = int(input('Informe o valor do raio da esfera: '))

print(f'Volume da esfera = {volume_esfera(n)}')