from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)

    def ficha(self):
        conteudo = f'Nome real:  [black on blue]{self.nome}[/black on blue]'
        conteudo += '\nJogos favoritos:'
        for x in self.favoritos:
            conteudo += f'\n:video_game: [blue]{x}[/blue]'
        ficha = Panel(conteudo,title=f'Jogador <{self.nick}>',width=50)
        print(ficha)

j1 = Gamer("Fabricio da Silva", "detonador 2025")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

j2 = Gamer("Olivia de Souza", "peach_raivosa")
j2.add_favoritos("Mario Bros.")
j2.add_favoritos("Call of Duty")
j2.ficha()