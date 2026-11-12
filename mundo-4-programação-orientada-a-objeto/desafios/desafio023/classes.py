from abc import ABC,abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        super().__init__()
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * self.qtd_lados

q1 = Quadrado(12)
print(q1.perimetro())
#Exercicio nao concluido ainda...