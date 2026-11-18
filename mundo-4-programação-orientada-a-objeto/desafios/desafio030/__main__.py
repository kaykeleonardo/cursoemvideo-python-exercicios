from classes import *
from rich import print,inspect

def main():
    c = Credencial()
    c.senha = str(input("Digite uma senha: "))

    c.validar("Senha1234")

if __name__ == "__main__":
    main()