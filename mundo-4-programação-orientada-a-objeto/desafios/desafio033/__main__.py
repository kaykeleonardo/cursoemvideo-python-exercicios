from classes import *
from rich import print, inspect

def main():
    a1 = Aluno("Maria",2000,'ADS')
    inspect(a1, private=True, methods=True)
    a1.add_curso('teste')
    a1.nascimento = 2029
    inspect(a1, private=True, methods=True)

if __name__ == "__main__":
    main()