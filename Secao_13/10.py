

arquivo_entrada = '10_arqu.txt'

try:
    with open(arquivo_entrada, 'r') as arquivo_entrada:
        conteudo_arquivo_entrada = arquivo_entrada.readlines()

        arquivo_saida = open('10_arqu_saida.txt', 'w')

        cidades = list()

        for linha in conteudo_arquivo_entrada:
            if linha != '\n':
                # print(linha.split(','))
                cidades.append(linha.split(','))

        maior_populacao = list()

        nome = ''
        habitantes = maior = 0

        for cidade in cidades:
            print(f'{cidade[0]} -> {cidade[1]} ')

            if float(cidade[1]) > maior:
                # Recebe a quantidade de habitantes
                maior = float(cidade[1])

                # Guarda o nome da cidade e dos habitantes para ser printado ao final.

                nome = cidade[0]
                habitantes = cidade[1]

        # retirando os espaços anteriores
        # habitantes = habitantes.replace(' ', '')

        # print(
        #     f'\nCidade de maior população: {nome}\nQuantidade de Habitantes: {habitantes}')

        maior_populacao.append(nome)
        maior_populacao.append(habitantes)

        arquivo_saida.writelines(maior_populacao)

        arquivo_saida.close
        print(f'O arquivo de saída foi fechado? [{arquivo_saida.closed}]')

except FileNotFoundError:
    print('>>> Arquivo não existe! <<<')
