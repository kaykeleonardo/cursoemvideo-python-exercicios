class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

g1 = Gafanhoto()
g1.nome = "Calebe"
g1.idade = 13
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Felipe"
g2.idade = 34
print(g2.mensagem())