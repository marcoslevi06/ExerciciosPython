

A = []
i = 0

while len(A) < 15:
    nota = float(input(f'Digite {i + 1}ª nota: '))

    if 1 <= nota <= 10:
        A.append(nota)
        i += 1


print(f'Média das {len(A)} notas = {sum(A) / len(A):.2f}')
