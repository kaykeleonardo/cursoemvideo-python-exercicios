from classes import *
from rich import print, inspect
from rich.traceback import install

def main():
    c1 = ContaBancaria(12,"Cleber",1200, "Gafanhoto")
    c1.nome = "Rafael"
    c1.depositar(500)
    c1.sacar(200)
    inspect(c1, private=True,methods=True)

if __name__ == "__main__":
    main()