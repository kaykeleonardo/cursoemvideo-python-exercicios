from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f'[blue]{self.nome.center(30, ' ')}[/blue]'
        conteudo += f'{'-' * 30}'
        precof = f"R${self.preco:,.2f}"
        conteudo += f"[green]{precof.center(30, '-')}[/green]"
        etiqueta = Panel(conteudo, title="Produto", width=34)
        print(etiqueta)

p1 = Produto("Galaxy Watch 7", 1500)
p1.etiqueta()

p2 = Produto("Iphone 15 Pro Max", 4650)
p2.etiqueta()