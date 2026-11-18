from classes import *
from rich import print, inspect

def main():
    r = Retangulo()
    r.medidas = (3,5)

    inspect(r, private=True, methods=True)
    print(r.medidas)

if __name__ == "__main__":
    main()