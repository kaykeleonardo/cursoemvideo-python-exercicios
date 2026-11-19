from abc import ABC, abstractmethod
from datetime import date
from rich import print, inspect

class Pessoa(ABC):
    def __init__(self, nome:str, nascimento:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano:int):
        if ano > date.today().year or ano < 1910 or not isinstance(ano, int):
            print("Ano Invalido")
        else:
            self._nascimento = ano

    @property
    def idade(self):
        idade = date.today().year - self._nascimento 
        return idade

    @idade.setter
    def idade(self, idade):
        raise PermissionError(f"Você não pode alterar a idade diretamente, somente o ano de nascimento.")

class Aluno(Pessoa):
    def __init__(self, nome:str, nascimento:int, curso:str):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ['ADS', 'ES', 'CC', 'SI']
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, atual:str):
        atual = atual.strip()
        if len(atual) < 3 or len(atual) > 5:
            print("Nome de curso invalido, tente novamente.")
        else:
            self._curso = atual

    def add_curso(self, curso:str):
        curso = curso.upper()

        if curso not in self.cursos_oficiais:
            if 3 <= len(curso) <= 6 and isinstance(curso, str):
                self.cursos_oficiais.append(curso) 
            else:
                print("Esse curso não pode ser adicionado.")
    

