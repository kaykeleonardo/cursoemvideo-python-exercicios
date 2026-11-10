from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")

tabela.add_column("Nome", justify="right", style="blue")
tabela.add_column("Preço",justify="center",style="red")

tabela.add_row("Lapis", "300")
tabela.add_row("Painel", "2500")

print(tabela)
