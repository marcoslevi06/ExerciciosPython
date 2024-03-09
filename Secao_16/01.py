
class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    
    def get_nome(self):
        return f'{self.__nome}'
    
    def get_idade(self):
        return f'{self.__idade}'
    
    def get_altura(self):
        return f'{self.__altura}'
    
    def set_nome(self, novo_novo):
        self.__nome = novo_novo
    
    def set_idade(self, nova_idade):
        self.__idade = nova_idade
    
    def set_altura(self, nova_altura):
        self.__altura = nova_altura


Pessoa1 = Pessoa('Levi', 23, 1.80)

# Printando Nome, idadae e altura através do método get.
print(f'Nome: {Pessoa1.get_nome()}  Idade: {Pessoa1.get_idade()}    Altura: {Pessoa1.get_altura()}')

# Setando novos valores com o método set.
Pessoa1.set_nome('Marcos Levi')
Pessoa1.set_idade(24)
Pessoa1.set_altura(1.90)

# Printando o novo nome, idade e taltura.
print(f'\nNovo nome: {Pessoa1.get_nome()}   Nova Idade: {Pessoa1.get_idade()}   Nova Altura: {Pessoa1.get_altura()}')