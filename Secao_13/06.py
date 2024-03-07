

nome_do_arquivo = '06_arqu.txt'


conta_letras = dict()

try:
    with open(nome_do_arquivo, 'r') as arquivo_6:
        conteudo_arquivo_6 = arquivo_6.readlines()

        for linha in conteudo_arquivo_6:
            for simbolo in linha:

                if simbolo.isalpha():
                    simbolo = simbolo.lower()
                    conta_letras[simbolo] = conta_letras.get(simbolo, 0) + 1

        print(f' >>> {conta_letras}')

        for chave, valor in conta_letras.items():
            print(f'>>> {chave.upper()}: {valor}')


except FileNotFoundError:
    print('>>> ARQUIVO NÃO EXISTE. <<<<')
