from classes import *
from rich import inspect

def main():
    p1 = Guerreiro("Cleiton", 1000)
    p2 = Mago("Roberto", 800)

    p1.curar()
    p2.curar()

    p1.atacar(p2, 250)
    p2.atacar(p1, 300)

    p1.curar()
    p2.curar()

    p2.atacar(p1, 50)
    p1.curar()
    p1.curar()

    inspect(p1)
    inspect(p2)

if __name__ == '__main__':
    main()