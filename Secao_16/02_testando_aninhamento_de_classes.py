
class Agenda:

    def __init__(self, nome_dono):
        self.__nome_dono_da_agenda = nome_dono
        self.__lista_contatos = list()
    
    def get_dono_agenda(self):
        
        return f'{self.__nome_dono_da_agenda}'
    
    def get_lista_de_contatos(self):
        nomes_contatos = [(contato.get_nome_contato(), contato.get_idade_contato(), contato.get_altura_contato()) for contato in self.__lista_contatos]
        return nomes_contatos
    
    def armazena_contato_na_agenda(self, nome, idade, altura):
        
        if self.quantidade_contatos() >= 10:
            return print('A lista de contatos está cheia.')
        
        novo_contato = Agenda.Contato(nome_contato=nome, idade_contato=idade, altura_contato=altura)
        self.__lista_contatos.append(novo_contato)

        return novo_contato, print('Contato criado com sucesso.')
    
    def remove_contato_na_agenda(self, contato):

        if contato in self.__lista_contatos:
            self.__lista_contatos.remove(contato)
            print('REMOVIDO COM SUCESSO.')
        else:
            print('Contato não encontrado.')
    
    def quantidade_contatos(self):
        return len(self.__lista_contatos)

    # Subclasse específica para salvar os contatos na agenda.
    class Contato:
        def __init__(self, nome_contato, idade_contato, altura_contato):
            self.__nome_contato = nome_contato
            self.__idade_contato = idade_contato
            self.__altura_contato = altura_contato

        # Métodos que cuidam das responsabilidades da subclasse Contato.
        def get_nome_contato(self):
            return f'{self.__nome_contato}'
        
        def get_idade_contato(self):
            return f'{self.__idade_contato}'
        
        def get_altura_contato(self):
            return f'{self.__altura_contato}'



agenda_1 = Agenda('Levi')

# Criando a primeira agenda e seus contatos.

contato_1 = agenda_1.armazena_contato_na_agenda('Sued', 22, 1.80)
contato_2 = agenda_1.armazena_contato_na_agenda('Cris', 25, 1.70)

# Printando os contatos.
print(agenda_1.get_lista_de_contatos())

# Removendo contato.
agenda_1.remove_contato_na_agenda(contato_2)

# Printando novamente os contatos.
print(agenda_1.get_lista_de_contatos())