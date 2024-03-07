


with open('votacao_fifa_2023.txt', 'r') as arqu_votacao:
    conteudo_arquivo = arqu_votacao.readlines()
    print(conteudo_arquivo)

    for linha in conteudo_arquivo:
        # print(linha)
        if linha == 'inicicio':
            versao_1 = linha.split('|')
            print(versao_1)