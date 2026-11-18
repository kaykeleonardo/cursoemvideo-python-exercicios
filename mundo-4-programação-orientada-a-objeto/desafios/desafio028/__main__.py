from classes import *
from rich import print, inspect

def main():
    t = Termostato()
    try:
        t.temperatura = 42.3
    except Exception as e:
        print(f"Houve um erro: {e}")

    print(f"A temperatura atual é {t.ftemperatura}")

if __name__ == "__main__":
    main()