from time import sleep
from rich import print
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.atual = 1
        print(f":book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/red]' que tem [green]{self.paginas} páginas[/green] no total. Você agora esta na [yellow]página {self.atual}[/yellow][/blue]")

    def avancar_paginas(self, avanco):
        if self.atual >= self.paginas:
            print(f'O livro tem somente [red]{self.paginas} páginas[/red], você já esta no final.')
        else:
            contador = 0
            for x in range(1, avanco + 1):
                contador +=1
                self.atual += 1
                print(f'Pag{self.atual}', end=' ▶︎ ')
                sleep(0.5)
                if self.atual == self.paginas:
                    break
            print(f'[blue]Você avançou {contador} páginas e agora esta na[/blue] [yellow]página {self.atual}[/yellow]')
            
            
            if self.atual == self.paginas:
                print(f":closed_book: [red]Você chegou ao final do Livro '{self.titulo}'[/red]")

l1 = Livro("Carros",20)
l1.avancar_paginas(5)
l1.avancar_paginas(5)
l1.avancar_paginas(5)
l1.avancar_paginas(100)

print()
l2 = Livro("Motos", 30)
l2.avancar_paginas(15)
l2.avancar_paginas(4)
l2.avancar_paginas(34)


    