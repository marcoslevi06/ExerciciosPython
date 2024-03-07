

nome_arquivo_1 = '09_arqu_1.txt'
nome_arquivo_2 = '09_arqu_2.txt'

try:
    with open(nome_arquivo_1, 'r') as arquivo_1:
        conteudo_arquivo_1 = arquivo_1.readlines()

    with open(nome_arquivo_2, 'r') as arquivo_2:
        conteudo_arquivo_2 = arquivo_2.readlines()

    # print(conteudo_arquivo_1)
    # print(conteudo_arquivo_2)

    novo_arquivo = open('09_novo_arqu.txt', 'w')

    # for linha in conteudo_arquivo_2:
    novo_arquivo.writelines(conteudo_arquivo_2)
    novo_arquivo.writelines(conteudo_arquivo_1)

    novo_arquivo.close()

    print(f'\nO arquivo {novo_arquivo.name} foi escrito com sucesso.')
    print(
        f'O arquivo {novo_arquivo.name} está fechado? [{novo_arquivo.closed}]')

except FileNotFoundError:
    print('>>> O arquivo não existe! <<<')
