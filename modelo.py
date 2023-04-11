class Programa:
     def __init__(self, nome, ano,):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

     @property
     def nome (self):
        return self._nome

     @property
     def likes(self):
        return self._likes
     
     @nome.setter
     def nome(self, novo_nome):
        self._nome = novo_nome.titled()

     def dar_like(self):
        self._likes += 1

     def __str__(self):
         return f'Nome --> {self._nome} - Ano --> {self.ano} - Likes --> {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
         return f'Nome --> {self._nome} - Ano --> {self.ano} - Duração --> {self.duracao} Min - Likes --> {self._likes}'

        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
         return f'Nome --> {self._nome} - Ano --> {self.ano} - Temporada --> {self.temporadas} Temporadas - Likes --> {self._likes}'


class Playlist:
    def __init__(self, nome, programa):
      self.nome = nome.title()
      self._programa = programa

    @property
    def listagem (self):
        return self._programa
        
    @property
    def tamanho (self):
        return len(self._programa)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tdmp = Filme('Todo mundo em panico', 1999, 100)
atlanta = Serie('atlanta', 2018, 2)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
vingadores.dar_like()
tdmp.dar_like()
tdmp.dar_like()
tdmp.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()


filmes_e_series = [vingadores, atlanta, demolidor, tdmp]
playlist_fds = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho do playlist {len(playlist_fds.listagem)}')

print(demolidor in playlist_fds.listagem)

for programa in playlist_fds.listagem:
   print(programa)

