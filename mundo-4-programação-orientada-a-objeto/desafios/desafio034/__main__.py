from classes import *
from rich import print, inspect

def main():
    f = Gerente("Fabio", 1000)
    f.salario = 2000
    print(f)
if __name__ == "__main__":
    main()