from classes import *
from rich import print, inspect

def main():
    a1 = Aluno("Maria",2000,'ADS')
    print(a1.exibir_dados())
    
if __name__ == "__main__":
    main()