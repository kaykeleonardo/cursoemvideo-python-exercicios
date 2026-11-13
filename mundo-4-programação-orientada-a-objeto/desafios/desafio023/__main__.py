from rich import print, inspect
from classes import *

def main():
    q1 = Quadrado(5)
    c1 = Circulo(5)
    print(f"Um quadrado de lado {q1.lado} tem área de {q1.area()} e perimetro de {q1.perimetro()}.")
    print(f"Um circulo de raio {c1.raio} tem área de {c1.area()} e perimetro de {c1.perimetro()}.")

if __name__ == '__main__':
    main()