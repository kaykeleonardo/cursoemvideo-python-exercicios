from math import pi
from abc import ABC,abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        super().__init__()
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return f'{self.lado * self.qtd_lados:.2f}'

    def area(self):
        return f'{self.lado ** 2:.2f}'

class Circulo(Poligono):
    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return f'{2 * self.raio * pi:.2f}'

    def area(self):
        return f'{pi * (self.raio ** 2):.2f}'

