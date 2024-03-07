
while True:

    arquivo = open('01_arqu.txt', 'a+')

    entrada = input(
        'Digite algo a ser salvo em arquivo [p/ encerrar digite 0]: ')

    if entrada == '0':
        arquivo.close()
        print(f'Encerrando... Arquivo está fechado? {arquivo.closed}')
        break
    else:
        arquivo.write(entrada + '\n')
        print('Salvo com sucesso!')


print(f'\nLendo o arquivo...\n')

arquivo = open('01_arqu.txt', 'r')
print(arquivo.read())
print(f'Tipo do arquivo: {type(arquivo)}')

arquivo.seek(0)

print(f'\nLendo o arquivo linha por linha...\n')
print(f'Tipo do arquivo: {type(arquivo)}')
for linha in arquivo:
    print(f'Conteúdo: {linha}   Tipo: {type(linha)}')
