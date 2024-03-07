# Arquivo 1
# open(), read(), readline(), readlines(), seek(), closed(), close()
# w escreve, r leitura, a append, r+ leitura e escrita, w+ escrita e leitura

arquivo = open('arquivo.txt', 'r')

qtd_linhas = len(arquivo.readlines())

print(qtd_linhas)
arquivo.seek(0)
print(arquivo.read())

print(arquivo.closed)
arquivo.close()
print(arquivo.closed)
print('Fim do arquivo 1\n')

# Arquivo 2
# Bloco with, serve para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with
# read() retorna um tipo string, readline() retorna uma string, readlines() retorna uma lista de strings

with open('arquivo2.txt', 'r') as arquivo:
    print(f' >>> Printando o arquivo: {arquivo}')
    print(f' >>> Printando o tipo do arquivo: {type(arquivo)}')


    conteudo_read = arquivo.read(), arquivo.seek(0)
    conteudo_readline = arquivo.readline()
    conteudo_readlines = arquivo.readlines()
    
    print(f' Tipo do conteudo_READ: {type(conteudo_read)}')
    print(f' Tipo do conteudo_READLINE: {type(conteudo_readline)}')
    print(f' Tipo do conteudo_READLINES: {type(conteudo_readlines)}')

    print(f'\n Conteudo do arquivo READ: {conteudo_read}')
    print(f'\n Conteudo do arquivo READLINE: {conteudo_readline}')
    print(f'\n Conteudo do arquivo READLINES: {conteudo_readlines}')
print('Fim do arquivo 2\n')

# Arquivo 3
# Escrevendo em um arquivo

nome_arquivo = 'para_escrever.txt'

with open(nome_arquivo, 'w') as arquivo:
    arquivo.write('Escrevendo no arquivo\n')
    arquivo.write('Escrevendo no arquivo 2\n')
    arquivo.write('Escrevendo no arquivo 3\n')
    arquivo.write('Escrevendo no arquivo 4\n')

# r ->Abre para leitura - padrão
# w ->Abre para escrita - sobrescreve caso o arquivo já exista
# x ->Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera um erro FileExistsError
# a ->Abre para escrita, adicionando o conteúdo no final do arquivo 
# + ->Abre para o modo de atualização (leitura e escrita)
    

    