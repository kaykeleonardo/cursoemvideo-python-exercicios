from abc import ABC, abstractmethod
from rich import print
from random import randint

class Personagem(ABC):
    def __init__(self, nome, vida, golpes):
        super().__init__()
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

    def atacar(self, alvo, forca):
        golpe = self.golpes[randint(0,len(self.golpes) - 1)]
        print(f'[green]{self.nome}[/]([cyan]{self.vida}[/]) atacou [red]{alvo.nome}[/]([cyan]{alvo.vida}[/]) com [blue]{golpe}[/] e aplicou [cyan]{forca}[/] de força')
        alvo.receber_dano(forca)

    def receber_dano(self, dano):
        dano_real = randint(0,dano)
        self.vida -= dano_real
        print(f'[blue]{self.nome}[/blue] perdeu [red]{dano_real} pontos de vida[/]')
        

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        self.vida_inicial = vida
        movimentos = [
            "Golpe de Espada",
            "Estocada",
            "Escudada",
            "Corte Giratório",
            "Investida Brutal",
            "Quebra-Crânio",
            "Ataque Pesado",
            "Fúria Bárbara",
            "Lâmina Sísmica",
            "Execução",
            ]
        super().__init__(nome, vida, golpes = movimentos)

    def curar(self):
        cura = randint(1,100)
        dif_vida = self.vida_inicial - self.vida
        if cura > dif_vida:
            cura = dif_vida
            self.vida = self.vida_inicial
        else:
            self.vida += cura
        print(f'[blue]{self.nome}[/blue] usou uma atadura e [green]recuperou {cura} pontos[/green] de vida.')


class Mago(Personagem):
    def __init__(self, nome, vida):
        self.vida_inicial = vida
        movimentos = [
            "Bola de Fogo",
            "Raio Arcano",
            "Seta de Gelo",
            "Relâmpago em Cadeia",
            "Explosão Etérea",
            "Mísseis Mágicos",
            "Chuva de Meteoros",
            "Onda de Choque",
            "Prisão Astral",
            "Drenar Energia",
        ]
        super().__init__(nome, vida, golpes = movimentos)

    def curar(self):
        cura = randint(1,100)
        dif_vida = self.vida_inicial - self.vida
        if cura > dif_vida:
            cura = dif_vida
            self.vida = self.vida_inicial
        else:
            self.vida += cura
        print(f'[blue]{self.nome}[/blue] usou uma magia de cura e [green]recuperou {cura} pontos[/green] de vida.')       




