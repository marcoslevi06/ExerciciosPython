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


