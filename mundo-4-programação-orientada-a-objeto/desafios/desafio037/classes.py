
from rich import print
from rich.panel import Panel

class Mensagem:
    def __init__(self, msg:str = "", tipo:str = "AVISO", icone:str = ":speech_balloon:"):
        self._msg = msg
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        mensagem = Panel(self._msg, title=f"{self._icone}{self._tipo}{self._icone}", style="bright_white on grey0")
        print(mensagem)


class Erro(Mensagem):
    def __init__(self, msg: str = "", tipo: str = "Erro", icone: str = ":prohibited:"):
        super().__init__(msg, tipo, icone)

    def mostrar(self):
        mensagem = Panel(self._msg, title=f"{self._icone}{self._tipo}{self._icone}", style="yellow1 on red1", width=40)
        print(mensagem)


class Alerta(Mensagem):
    def __init__(self, msg: str = "", tipo: str = "Alerta", icone: str = ":warning:"):
        super().__init__(msg, tipo, icone)

    def mostrar(self):
        mensagem = Panel(self._msg, title=f"{self._icone}{self._tipo}{self._icone}", style="grey0 on yellow1")
        print(mensagem)

