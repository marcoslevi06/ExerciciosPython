

nome_do_arquivo = '04_arqu.txt'


def verifica_letra(caractere):

    if caractere in 'aeiouAEIOU':
        return 'vogal'
    elif caractere.lower() in 'b c d f g h j k l m n p q r s t v x y w z':
        return 'consoante'

try:
    with open(nome_do_arquivo, 'r') as arquivo_4:
        conteudo_arquivo_4 = arquivo_4.readlines()

        cont_vogal = 0
        cont_consoante = 0

        for linha in conteudo_arquivo_4:
            for letra in linha:
                if verifica_letra(letra) == 'vogal':
                    cont_vogal += 1
                elif verifica_letra(letra) == 'consoante':
                    cont_consoante += 1
                else:
                    continue
    
    print(f'\nTotal de Vogais = {cont_vogal}\nTotal de Consoantes: {cont_consoante}')
except FileNotFoundError:
    print(f' >>> O arquivo {nome_do_arquivo} não existe! <<< ')