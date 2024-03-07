
n_caracteres = 0
n_linhas = 0
n_palavras = 0

var_teste = 0

nome_arquivo = '12_arqu.txt'

try:
    with open(nome_arquivo, 'r') as arquivo_12:
        conteudo_arquivo_12 = arquivo_12.readlines()

        for linha in conteudo_arquivo_12:
            n_linhas += 1

            for palavra in linha.split():

                # print(simbolo)
                # print(len(simbolo))
                
                n_caracteres += len(palavra)
                n_palavras += 1

        
        print(f'    O total de caracteres excluindo os espaços é: {n_caracteres}')
        print(f'    O total de palavras é: {n_palavras}')
        print(f'    O total de linhas é: {n_linhas}')

except FileNotFoundError:
    print('>>> Arquivo não existe <<<')