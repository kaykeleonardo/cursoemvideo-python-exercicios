from classes import *
from rich import print, inspect

def main():
    d = Diario("Banana")
    d.escrever("Java é bom")
    d.escrever("Vasco")
    d.escrever("CLUBE ATLETICO MINEIRO")

    d.ler("Banana")


if __name__ == "__main__":
    main()