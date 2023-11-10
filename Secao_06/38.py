
termo_pitagorico = 1000

# a² + b² = c²
# encontrar essa equivalência dessa equacao pra números de 1 até 1000

for a in range(1, 1001):
    for b in range(1, 1001):
        c = 1000 - a - b

        if a**2 + b**2 == c**2:
            print(f'{a}² + {b}² = {c}²')
