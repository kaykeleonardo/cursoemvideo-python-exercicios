from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        super().__init__()
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.5

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return f'R${self.frete:.2f}'



class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20

    def calc_frete(self):
        if self.distancia >= 50:
            self.frete = self.distancia * self.fator
            return f'R${self.frete:.2f}'
        else:
            return "Distancia minima 50km"


class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.50

    def calc_frete(self):
        if self.distancia <= 10:
            self.frete = self.distancia * self.fator
            return f'R${self.frete:.2f}'
        else:
            return "Raio maximo de 10km"

