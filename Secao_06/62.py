
from num2words import num2words

qtd_letras = 0

for i in range(1, 5):

    qtd_letras += len(num2words(i, lang='pt_BR'))
    print(f'{i} = {num2words(i, lang="pt_BR")},     Qtd de letras = {len(num2words(i, lang="pt_BR"))}')

print(f'Quantidade de letras: {qtd_letras}')