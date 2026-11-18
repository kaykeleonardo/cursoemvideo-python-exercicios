from rich import print

class Diario:
    def __init__(self, senhamestra = "admin"):
        self.__segredos = []
        self.__senha = senhamestra.strip()

    def escrever(self,msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg)

    def ler(self,senha):
        if senha.strip() == self.__senha:
            print(f"[green]DIARIO LIBERADO[/]")
            for x in self.__segredos:
                print(f'- {x}')
        else:
            print(f"[red]Senha Inválida[/]")

    @property
    def senha(self):
        raise PermissionError(f"Ninguem tem acesso as senhas")

    