class Programa:

    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self._likes}')


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes: {self.likes}'


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self.likes}'


class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
todomundo = Filme('todo mundo em pânico', 1999, 100)
demolidor = Serie('demolidor', 2016, 3)
jurassic = Filme('jurassic park', 1994, 120)

vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()

filmes_e_series = [ vingadores, atlanta, todomundo, demolidor ]

playlist_fds = Playlist('Fim de Semana', filmes_e_series)

print(f'Tamanho de "{playlist_fds.nome}": {len(playlist_fds)}')
print(f'Demolidor está na playlist? {demolidor in playlist_fds}')
print(f'Jurassic Park está na playlist? {jurassic in playlist_fds}')

for programa in playlist_fds:
    print(programa)
