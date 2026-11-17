from classes import *
from rich import print, inspect

def main():
    t = Termostato()
    t.temperatura = 41.2
    inspect(t, private=True, methods=True)
    print(f"A temperatura atual é {t.ftemperatura}")

if __name__ == "__main__":
    main()