
nome_do_arquivo = '11_arqu.txt'
palavra_buscada = input(
    'Qual palavra deseja buscar: ').lower().replace(' ', '')
cont = 0

try:
    with open(nome_do_arquivo, 'r') as arquivo_11:
        conteudo_arquivo_11 = arquivo_11.readlines()

        for linha in conteudo_arquivo_11:
            for palavra in linha.split():

                if palavra != '':
                    # print(palavra)
                    if palavra.lower() == palavra_buscada:
                        cont += 1

        print(
            f'O total de vezes que a palavra {palavra_buscada.title()} aparene no arquivo {arquivo_11.name} é {cont} vez(es).')
except FileNotFoundError:
    print('>>> Arquivo não encontrado. <<<')
