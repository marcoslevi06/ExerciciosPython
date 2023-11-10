

for i in range(1000, 9999 + 1):
    dois_primeiros = i // 100
    dois_ultimos = i % 100

    soma = dois_primeiros + dois_ultimos

    if soma**2 == i:
        print(f'({dois_primeiros} + {dois_ultimos})² = {i}')
