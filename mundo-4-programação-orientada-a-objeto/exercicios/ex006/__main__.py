from rich import inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno("Cleiton", 15, "Algebra Linear", "EB101")
    p1 = Professor("Marcos", 35, "Matematica", "Doutor")
    f1 = Funcionario("Amanda", 22, "Atendente", "Recepção")

    p1.fazer_aniversario()
    f1.fazer_aniversario()

    inspect(a1, methods=True)
    inspect(p1, methods=True)
    inspect(f1, methods=True)

if __name__ == '__main__':
    main()