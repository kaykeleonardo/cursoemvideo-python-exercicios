from rich import print

class Caneta:
    def __init__(self, cor = 'azul'):
        match cor.lower().strip():
            case "azul":
                escolha = "blue"
            case "verde":
                escolha = "green"
            case "vermelha":
                escolha = "red"
            case _:
                escolha = "white"

        self.cor = escolha
        self.tampa = False

    def destampar(self):
        self.tampa = True

    def escrever(self, msg):
        if self.tampa:
            print(f'[{self.cor}]{msg}[/{self.cor}]', end='')
        else:
            print(":stop_sign: A caneta esta tampada, você não pode escrever.")

    def quebrar_linha(self, num):
        if num > 0:
            print('\n' * (num - 1))

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem? ")
c1.quebrar_linha(1)
c2.escrever("Olá, Gafanhoto! ")
c3.escrever("Vamos exercitar!")
