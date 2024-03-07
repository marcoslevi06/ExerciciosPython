

# Estou assumindo que o arquivo 02.txt está na mesma pasta que este script.
# Caso contrário, é necessário informar o caminho completo do arquivo.
# E que o usuário abriria o arquivo 02.txt e escreveria algo nele.


nome_arquivo = '02_arqu.txt'

with open(nome_arquivo, 'r') as arquivo:
    
    print(f'\nConteúdo do arquivo {nome_arquivo}:')
    print(arquivo.read())
    # print(f'\nTipo do arquivo: {type(arquivo)}')

    # Retorna o cursor para o início do arquivo.
    arquivo.seek(0)
    
    # Retorna uma lista com as linhas do arquivo.
    linhas = arquivo.readlines()

    print(f'\nTipo retornado por arquivo.readlines():{type(linhas)}')
    print(f'\nConteúdo retornado por arquivo.readlines():\n{linhas}')
    print(f'\nQuantidade de linhas: {len(linhas)}')
