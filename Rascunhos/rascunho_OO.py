# Crie uma classe chamada Livro com os seguintes atributos: titulo, autor e paginas. Em seguida, crie um objeto da classe Livro com os valores "O Pequeno Príncipe", "Antoine de Saint-Exupéry" e 128. Imprima as informações do livro utilizando a formatação adequada. Por fim, crie um método chamado. ler() que incrementa o número de páginas lidas em 1 e imprima o novo valor de páginas lidas.

# class Livro:

#     def __init__(self, titulo, autor, paginas):
#         self.titulo = titulo.title()
#         self.autor = autor
#         self.paginas = paginas
#         self.paginas_lidas = 0

#     def ler(self, pagina):
#         if pagina > 0:
#             self.paginas_lidas += 1

#         return f'Página lida! Qtd pág lidas: {self.paginas_lidas}'

# livro_1 = Livro('Pequeno Príncipe', 'Antoine de saint-Exupéry', 128)

# print(
#     f'\n Nome do livro: {livro_1.titulo}, Quantidade de páginas lidas: {livro_1.paginas_lidas}')

# # Chamando método
# print(livro_1.ler(1))

# print(
#     f'\n Nome do livro: {livro_1.titulo}, Quantidade de páginas lidas: {livro_1.paginas_lidas}')


# Claro! Um exercício baseado nessa aula seria criar uma classe chamada "Livro" com os atributos "titulo", "autor" e "paginas". Em seguida, adicione os métodos getters e setters para cada um desses atributos. Por fim, crie um objeto da classe "Livro" e teste a funcionalidade dos métodos getters e setters.

# class Livro:

#     def __init__(self, titulo, autor, paginas):
#         self.__titulo = titulo.title()
#         self.__autor = autor
#         self.__paginas = paginas
#         self.paginas_lidas = 0

#     def ler(self, pagina):
#         if pagina > 0:
#             self.paginas_lidas += 1

#     @property
#     def titulo(self):
#         return f'Título do Livro: {self.__titulo}'

#     @property
#     def autor(self):
#         return f'Nome do autor: {self.__autor}'

#     @property
#     def paginas(self):
#         return f'Total de páginas: {self.__paginas}'

#     @titulo.setter
#     def titulo(self, novo_titulo):
#         self.__titulo = novo_titulo


# livro_1 = Livro('Pequeno Príncipe', 'Antoine de saint-Exupéry', 128)

# print(f'\n{livro_1.titulo}\n{livro_1.autor}\n{livro_1.paginas}')

# livro_1.titulo = 'Uma novo título qualquer aqui'

# print(f'\n{livro_1.titulo}')


# class Programa:
#     def __init__(self, nome, ano, likes):
#         self.__nome = nome
#         self.ano = ano
#         self.__likes = likes

#     @property
#     def nome(self):
#         return f'Nome: {self.__nome}'

#     @property
#     def likes(self):
#         return f'Qtd likes: {self.__likes}'

#     @nome.setter
#     def nome(self, novo_nome):
#         self.__nome = novo_nome

#     def dar_likes(self, like):
#         self.__likes += 1


# class Filme(Programa):
#     def __init__(self, nome, ano, likes, duracao):
#         super().__init__(nome, ano, likes)
#         self.duracao = duracao


# class Serie(Programa):
#     def __init__(self, nome, ano, likes, temporadas):
#         super().__init__(nome, ano, likes)
#         self.temporadas = temporadas


# filme_1 = Filme('Batman', 2010, 0, 120)
# filme_1.dar_likes(1)
# serie_1 = Serie('One Piece', 2010, 0, 1000)
# serie_1.dar_likes(1)

# print(filme_1.nome, filme_1.likes)
# print(serie_1.nome, serie_1.likes)

# filme_1.nome = 'Batman Cavaleiro das Trevas'
# serie_1.nome = 'Hunter x Hunter'
# filme_1.dar_likes(1)
# serie_1.dar_likes(1)
# print(filme_1.nome, filme_1.likes)
# print(serie_1.nome, serie_1.likes)

# Claro! Aqui está uma atividade sobre o conteúdo dessa aula: Atividade: Explorando o Polimorfismo Crie uma classe chamada "Programa" com os seguintes atributos: nome (string) duracao (integer) likes (integer) Crie duas classes filhas da classe "Programa": "Filme" com um atributo adicional "genero" (string) "Serie" com um atributo adicional "temporadas" (integer) Crie três objetos: um objeto da classe "Filme", um objeto da classe "Serie" e um objeto da classe "Programa". Adicione esses objetos a uma lista chamada "filmes_e_series". Utilizando um loop for, percorra a lista "filmes_e_series" e imprima o nome, a duração e os likes de cada programa. Utilize a função hasattr() para verificar se cada programa possui o atributo "temporadas" ou "duracao". Se possuir, imprima o valor correspondente. Reflita sobre como o polimorfismo foi aplicado nesse exemplo e como isso torna o código mais flexível.

# class Programa:
#     def __init__(self, nome, duracao, like):
#         self.nome = nome
#         self.duracao = duracao
#         self.like = like


# class Filme(Programa):
#     def __init__(self, nome, duracao, like, genero):
#         super().__init__(nome, duracao, like)
#         self.genero = genero


# class Serie(Programa):
#     def __init__(self, nome, duracao, like, temporadas):
#         super().__init__(nome, duracao, like)
#         self.temporadas = temporadas


# filme_1 = Filme('Batman', 100, 0, 'Ação')
# filme_2 = Filme('Miranha ', 110, 0, 'Ação e Aventura')
# filme_3 = Filme('Avatar', 120, 0, 'Fantasia')
# serie_1 = Serie('Hunter x Hunter', 20, 0, 10)

# lista_filmes = (filme_1, filme_2, filme_3, serie_1)

# for producao in lista_filmes:
#     if hasattr(producao, 'genero'):
#         print(
#             f'Nome: {producao.nome} | Duração: {producao.duracao} | Likes: {producao.like}  Gênero: {producao.genero}')
#     else:
#         print(
#             f'Nome: {producao.nome} | Duração: {producao.duracao} | Likes: {producao.like}  Temporadas: {producao.temporadas}')


# Claro! Um exercício baseado nessa aula seria criar uma nova classe chamada Livro que também herde da classe Programa. Essa classe deve ter um atributo autor e um método imprime() que imprime as informações do livro, incluindo o autor. Depois, crie alguns objetos da classe Livro e faça um loop para imprimir as informações de cada um deles utilizando o método imprime().

# class Programa:
#     def __init__(self, nome, duracao, like):
#         self.nome = nome
#         self.duracao = duracao
#         self.like = like


# class Filme(Programa):
#     def __init__(self, nome, duracao, like, genero):
#         super().__init__(nome, duracao, like)
#         self.genero = genero

#     def imprime(self):
#         print(
#             f'Nome: {self.nome} | Duracao: {self.duracao} | Likes: {self.like} | Autor: {self.genero}')


# class Serie(Programa):
#     def __init__(self, nome, duracao, like, temporadas):
#         super().__init__(nome, duracao, like)
#         self.temporadas = temporadas

#     def imprime(self):
#         print(
#             f'Nome: {self.nome} | Duracao: {self.duracao} | Likes: {self.like} | Temporadas: {self.temporadas}')


# class Livro(Programa):
#     def __init__(self, nome, duracao, like, autor):
#         super().__init__(nome, duracao, like)
#         self.autor = autor

#     def imprime(self):
#         print(
#             f'Nome: {self.nome} | Duracao: {self.duracao} | Likes: {self.like} | Autor: {self.autor}')


# filme_1 = Filme('Batman', 2010, 0, 120)
# serie_1 = Serie('One Piece', 2010, 0, 1000)
# livro_1 = Livro('O Capital', 2010, 0, 'Carlos Marques')

# play_list = (filme_1, serie_1, livro_1)

# for producao in play_list:
#     producao.imprime()


# Claro! Aqui está um exercício baseado na aula:

# Crie uma classe chamada Livro que represente um livro. Essa classe deve ter os seguintes atributos: titulo, autor e ano. Além disso, implemente os métodos especiais __str__() e __repr__() na classe Livro.

# O método __str__() deve retornar uma string formatada com as informações do livro, como "Título: {titulo}, Autor: {autor}, Ano: {ano}". O método __repr__() deve retornar uma representação do objeto que seja de fácil leitura para o computador.

# Em seguida, crie alguns objetos do tipo Livro e teste os métodos __str__() e __repr__() para verificar se estão retornando as informações corretas.

# Esse exercício irá ajudar a fixar o conceito de métodos especiais em Python e como utilizá-los para representar objetos de forma textual e para o próprio computador.


class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self) -> str:
        return f'Título: {self.titulo} | Autor: {self.autor} | Ano:{self.ano}'
    
    def __repr__(self):
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', ano={self.ano})"
    

livro_1 = Livro('HPE', 'E.K Hunt', 1976)

print(repr(livro_1))
print(livro_1)