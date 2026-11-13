from classes import *
from rich import print
from rich.table import Table

def main():
    dist = 100
    transportes = [Moto(dist),Caminhao(dist),Drone(dist)]
    tabela = Table(title="Tabela de Fretes")

    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    for x in transportes:
        tabela.add_row(f'{dist}Km', type(x).__name__, x.calc_frete())
    print(tabela)
if __name__ == "__main__":
    main()