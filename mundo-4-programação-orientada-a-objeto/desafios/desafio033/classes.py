from abc import ABC, abstractmethod
from datetime import date

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
        if not isinstance(ano, int) or ano > date.today().year or ano < 1910:
            raise ValueError("Ano Invalido")
        self._nascimento = ano

    @property
    def idade(self):
        idade = date.today().year - self._nascimento 
        return idade

    @idade.setter
    def idade(self, idade):
        raise PermissionError(f"Você não pode alterar a idade diretamente, somente o ano de nascimento.")

    @abstractmethod
    def exibir_dados(self):
        pass

    
class Aluno(Pessoa):
    cursos_oficiais = ['ADS', 'ES', 'CC', 'SI']

    def __init__(self, nome:str, nascimento:int, curso:str):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, atual:str):
        if not isinstance(atual, str):
            raise TypeError("O curso deve ser um texto.")
        atual_formatado = atual.strip().upper()
        if atual_formatado not in self.cursos_oficiais:
            raise ValueError(f"O curso {atual_formatado} não esta presente na lista de cursos.\nCursos disponiveis: {self.cursos_oficiais}")
        self._curso = atual_formatado

    def add_curso(self, curso:str):
        if not isinstance(curso, str):
            raise TypeError("O nome do curso deve ser um texto.")
        curso_formatado = curso.strip().upper()

        if not (3 <= len(curso_formatado) <= 6):
            raise ValueError("O nome do curso deve ter entre 3 e 6 caracteres.") 

        if curso_formatado not in self.cursos_oficiais:
            self.cursos_oficiais.append(curso_formatado)

    def exibir_dados(self):
        return f"Aluno: {self._nome} | Idade: {self.idade} | Curso: {self.curso}"
    

