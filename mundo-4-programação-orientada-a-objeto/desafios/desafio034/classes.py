from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome:str, salario:float = 1_621):
        self.nome = nome 
        self.__salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor:float):
        if valor is None:
            raise ValueError("Valor inválido")
        else:
            if valor >= self.__salario:
                self.__salario = valor
            else:
                raise ValueError("Operação não permitida, você não pode diminuir o salário.")
        
    def __str__(self):
        return f"{self.nome} tem o salario de R${self.__salario:.2f} e o bonus é de R${self.calcular_bonus():.2f} por ser {self.__class__.__name__}"
    
class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15

class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10

class Designer(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.08


