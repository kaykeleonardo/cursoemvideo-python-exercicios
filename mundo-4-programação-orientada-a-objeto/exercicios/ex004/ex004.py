from rich import inspect

class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula():
        pass


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto():
        pass

a1 = Aluno("Cleiton", 15, "Algebra Linear", "EB101")
p1 = Professor("Marcos", 35, "Matematica", "Doutor")
f1 = Funcionario("Amanda", 22, "Atendente", "Recepção")

p1.fazer_aniversario()
f1.fazer_aniversario()

inspect(a1, methods=True)
inspect(p1, methods=True)
inspect(f1, methods=True)