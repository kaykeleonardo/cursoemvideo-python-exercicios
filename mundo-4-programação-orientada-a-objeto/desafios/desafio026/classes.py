from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import inspect,print

class Funcionario(ABC):
    def __init__(self, nome, bruto):
        super().__init__()
        self.nome = nome
        self.sal_bruto = bruto
        self.salario = 0
        self.sal_min = 1612.00
        self.inss = 7.5
        

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        qtd_minimo = self.salario / self.sal_min
        conteudo = f'O salário de [blue]{self.nome}[/blue] ([violet]{self.__class__.__name__}[/violet]) é de [green]R${self.salario:.2f}[/green] e corresponde a [yellow]{qtd_minimo:.1f} salários mínimos[/yellow].'
        dados = Panel(conteudo,title="Análise de Salário", width=50)
        print(dados)
        

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, qtd_horas):
        super().__init__(nome, bruto = valor_hora * qtd_horas)

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * (self.inss / 100))


class Mensalista(Funcionario):
    def __init__(self, nome, liquido):
        super().__init__(nome, bruto = liquido)

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * (self.inss / 100))

