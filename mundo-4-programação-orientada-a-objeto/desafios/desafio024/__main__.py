from rich import print
from classes import *

def main():
    c1 = Cafe()
    c2 = Cha()
    l1 = Leite()

    c1.preparar()
    print()
    c2.preparar()
    print()
    l1.preparar()


if __name__ == "__main__":
    main()