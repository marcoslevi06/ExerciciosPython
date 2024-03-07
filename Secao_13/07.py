
nome_arquivo = '07_arqu.txt'

try:
    with open(nome_arquivo, 'r') as arquivo_7:
        conteudo_arquivo_7 = arquivo_7.readlines()

        novo_arquivo = open('07_novo_arqu.txt', 'w')

        for linha in conteudo_arquivo_7:
            linha_novo_arquivo = ''
            for simbolo in linha:
                linha_novo_arquivo += '*' if simbolo.lower() in 'aeiou' else str(simbolo)

            novo_arquivo.write(linha_novo_arquivo)
            print(linha_novo_arquivo)

        novo_arquivo.close()
except FileNotFoundError:
    print('>>> ARQUIVO NÃO ENCONTRADO. <<<<')
