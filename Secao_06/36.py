

soma_dos_quadrados = quadrado_da_soma = 0

for i in range(1, 101):
    soma_dos_quadrados += (i**2)

for i in range(1, 101):
    quadrado_da_soma += i

quadrado_da_soma = quadrado_da_soma**2

print(
    f'Diferença entre a soma dos quadrados e o quadrado da soma = {quadrado_da_soma - soma_dos_quadrados}')
