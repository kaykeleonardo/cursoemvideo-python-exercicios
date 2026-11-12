from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O aluno {self.nome} fez a matricula no curso {self.curso}. Sua turma é a {self.turma}!')

    def estudar(self):
        print(f'{self.nome} está estudando.')


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'Professor(a) {self.nome} esta dando aula!')

    def estudar(self):
        print(f'O professor(a) esta estudando para melhorar sua especialidade em {self.especialidade}')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'{self.nome} bateu ponto no setor {self.setor}.')

    def estudar(self):
        print(f'{self.nome} esta estudando para melhorar no cargo de {self.cargo}')