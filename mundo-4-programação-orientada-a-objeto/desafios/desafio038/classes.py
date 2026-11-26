from typing import Self


class Produto:
    def __init__(self, nome:str, preco:float=0):
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        return f"{self.nome} ({formata_preco(self.preco)})"


class Carrinho:
    def __init__(self, produtos:list=None):
        self.produtos = produtos if produtos else []

    @property
    def total(self):
        return sum(p for p in self.produtos)

    def __add__(self, outro):
        if isinstance(outro, Produto):
            return Carrinho(self.produtos + [outro])
        elif isinstance(outro, Carrinho):
            return Carrinho(self.produtos + outro.produtos)
        else:
            raise TypeError("Entrada de dados invalida")

    def __str__(self):
        linha = "\n" + "-" * 30
        itens = ",".join((str(p) for p in self.produtos))
        return f"{self.produtos} - Total: {formata_preco(self.total)}"

def formata_preco(valor:float):
    import locale
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    return locale.currency(valor, grouping=True)