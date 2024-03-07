
nome_do_arquivo = '03_arqu.txt'

try:
    with open(nome_do_arquivo, 'r') as arquivo:

        conteudo_arquivo3 = arquivo.readlines()

        cont_vogal_total = 0

        for conteudo_da_linha in conteudo_arquivo3:
            cont_vogal_linha = 0
            for letra in conteudo_da_linha:

                if letra.lower() in 'aeiou':
                    cont_vogal_linha += 1
                    cont_vogal_total += 1

            print(f'Quantidade de vogais na linha: {conteudo_da_linha} -> {cont_vogal_linha}')
        print(f'Quantidade total de vogais: {cont_vogal_total} ')
        
except FileNotFoundError:
    print(f'Arquivo {nome_do_arquivo} não encontrado.')