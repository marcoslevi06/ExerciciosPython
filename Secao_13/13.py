import re


def valida_nome(nome):

    nome_tradado = ' '.join(nome.title().split())
    return nome_tradado

def valida_numero(numero):
    numero_padrao = re.compile()

# nome_teste = 'Marcos Levi     Pinheiro            moreira             '
# print(valida_nome(nome=nome_teste))

try:
    with open('13_arqu_agenda.txt', 'w+') as arquivo_13:

        agenda = []
        iD = 0 

        while True:

            nome_contato = input(
                'Digite o nome do contato [digite 0 p/ encerrar]: ').title().strip()
            numero_contato = input(
                'Digite o numero do contato [digite 0 p/ encerrar]: ')

            if nome_contato == '0' or numero_contato == '0':
                print(' >>> FIM <<< ')
                break

            contato = {'id': iD, 'nome': valida_nome(nome=nome_contato), 'numero': numero_contato}
            agenda.append(contato)
            iD += 1

            string = str(agenda)
            arquivo_13.write(string)

except FileNotFoundError:
    print(' >>> ARQUIVO NÃO ENCONTRADO. <<< ')
