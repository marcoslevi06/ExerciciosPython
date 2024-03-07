
nome_arquivo = '08_arqu.txt'

try:
    with open(nome_arquivo, 'r') as arquivo_8:
        conteudo_arqu_8 = arquivo_8.readlines()

        # print(conteudo_arqu_8)
        novo_arquivo = open('08_novo_arqu.txt', 'w')

        for linha in conteudo_arqu_8:
            for letra in linha:
                # print(letra)
                if letra.isalpha():
                    novo_arquivo.write(letra.upper())
                else:
                    novo_arquivo.write(letra)

        novo_arquivo.close()

        print(f'\nO arquivo {novo_arquivo.name} foi escrito com sucesso.')
        print(f'O arquivo {novo_arquivo.name} está fechado? [{novo_arquivo.closed}]')
        
except FileNotFoundError:
    print('>>> ARQUIVO NÃO ENCONTRADO. <<<<')
