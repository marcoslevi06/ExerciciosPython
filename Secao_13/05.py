

nome_do_arquivo = '05_arqu.txt'
caractere = input('Qual caractere deseja contar? ').lower()


try:
    with open(nome_do_arquivo, 'r') as arquivo_5:
        conteudo_arquivo_5 = arquivo_5.readlines()

        cont_caractere = 0

        for linha in conteudo_arquivo_5:
            for simbolo in linha:
                if caractere == simbolo.lower():
                    cont_caractere += 1

        print(
            f'Total de caracteres [{caractere}] no arquivo {nome_do_arquivo}: {cont_caractere}')
except FileNotFoundError:
    print('>>> ARQUIVO NÃO EXISTE. <<<<')
