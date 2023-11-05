
prova1 = float(input('Digite a primeira nota: '))
prova2 = float(input('Digite a segunda nota: '))
prova3 = float(input('Digite a terceira nota: '))

media = ((prova1 * 1) + (prova2 * 1) + (prova3 * 2)) / 4

if media >= 60:
    print(f'Sua média foi {media:.2f}. Você está aprovado.')
else:
    print(f'Sua média foi {media:.2f}. Você está reprovado.')
