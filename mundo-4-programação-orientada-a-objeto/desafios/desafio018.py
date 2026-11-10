from rich import print
from rich.panel import Panel
from rich.traceback import install
install()
class Churrasco:
    consumo = 0.4 #Kg
    precoKg = 82.40 #R$
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quantidade = quant

    def calcular_qtd_carne(self) -> float:
        return self.quantidade * Churrasco.consumo

    def calcular_custo_total(self) -> float:
        return Churrasco.precoKg * self.calcular_qtd_carne()

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.quantidade
    
    def analisar(self):
        conteudo = f'''Analisando [green]{self.titulo}[/green] com [blue]{self.quantidade}[/blue] convidados
Cada participante comerá {Churrasco.consumo}Kg e cada Kg custa R${Churrasco.precoKg}
Recomendo [blue]comprar {self.calcular_qtd_carne():.3f}Kg[/blue] de carne
O custo total será de [green]R${self.calcular_custo_total():.2f}[/green]
Cada pessoa pagará [yellow]R${self.calcular_custo_individual():.2f}[/yellow] para participar.'''
        
        analisar = Panel(conteudo,title=self.titulo,width=90)

        print(analisar)

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()