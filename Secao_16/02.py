
class Agenda:

    def __init__(self, nomeDono, tipoAgenda):
        self.__nomeDono = nomeDono.title()
        self.__tipoAgenda = tipoAgenda
        self.__listaDeContatos = []

    def armazena_contato(self, nome, idade, altura):
    
        if self.quantidade_contatos() >= 10:
            return print('\nLimite da agenda foi atingido. Contato não foi criado.')
        
        contat = {
                'nome': nome,
                'idade': idade,
                'altura': altura,
                }

        self.__listaDeContatos.append(contat)

    def remove_contato(self, nomeContato):
        nome_buscado = nomeContato.upper()
        indice = 0

        for contato in self.__listaDeContatos:

            if contato['nome'].upper() == nome_buscado:
                self.__listaDeContatos.pop(indice)        
                return f'{nome_buscado} foi excluído com sucesso.'
            
            indice += 1

        return f'{nome_buscado} não foi encontrado.'

    def quantidade_contatos(self):
        return len(self.__listaDeContatos)
    
    def get_buscaPorPessoa(self, nomeContato):
        nomeBuscado = nomeContato.upper()
        indice = 0

        for contato in self.__listaDeContatos:
            
            indice += 1

            if contato['nome'].upper() == nomeBuscado:
                return f'\nO contato do(a) {nomeBuscado} está na posição {indice} da sua agenda.'

        return f'\n{nomeBuscado} não foi encontrado.'
    
    def get_buscaPorPosicao(self, posicao):
        indice = posicao - 1

        if posicao <= len(self.__listaDeContatos):
            return f'\nO contato que está na posição {posicao} da sua agenda é: {self.__listaDeContatos[indice]["nome"]}'.upper()
        
        return f'Posição não encontrada.'

    
    def get_listaContatos(self):
        return self.__listaDeContatos
    
    def info_sobre_agenda(self):
        return f' Dono = {self.__nomeDono} Tipo = {self.__tipoAgenda} Quantidade de contatos salvos = {self.quantidade_contatos()}.'.upper()

    def lista_agenda(self):

        print(f'\nAtuais contatos da agenda de {self.__nomeDono}:')
        
        for contato in self.__listaDeContatos:
            print(f'Nome: {contato["nome"]} Idade: {contato["idade"]} Altura: {contato["altura"]}')

# Criando a primeira agenda de contatos.   
agenda_1 = Agenda('Marcos', 'Agenda de Contatos.')

# Criando os contatos da agenda.
agenda_1.armazena_contato('Levi', 23, 1.80)
agenda_1.armazena_contato('Sued', 22, 1.75)
agenda_1.armazena_contato('Jair', 20, 1.75)
agenda_1.armazena_contato('Jaime', 20, 1.75)
agenda_1.armazena_contato('Léo Flex', 20, 1.95)
agenda_1.armazena_contato('Rafael', 20, 1.75)
agenda_1.armazena_contato('Cris', 25, 1.75)
agenda_1.armazena_contato('Tijonelson', 24, 1.75)
agenda_1.armazena_contato('Brenim', 25, 1.87)
agenda_1.armazena_contato('Thainá', 22, 1.85)

# Testando a remoção de algum contato.
print(agenda_1.remove_contato('levi'))
print(agenda_1.remove_contato('Thainá'))
# Buscando pelo nome da Pessoa.
print(agenda_1.get_buscaPorPessoa('Luiz Cafezinho'))
print(agenda_1.get_buscaPorPessoa('TIjonelson'))

# Imprimindo agenda.
agenda_1.lista_agenda()

# Busando por posição.
print(agenda_1.get_buscaPorPosicao(3))
print(agenda_1.get_buscaPorPosicao(9))
print(agenda_1.get_buscaPorPosicao(10))

