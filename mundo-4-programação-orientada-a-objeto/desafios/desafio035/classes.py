from abc import ABC, abstractmethod
class Arquivo(ABC):
    def __init__(self, nome:str, ext:str, tam:int):
        self.nome = nome
        self._extensao = None
        self.tamanho = tam
        self.extensao = ext

    @abstractmethod
    def abrir(self):
        pass

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext:str):
        formatos = ['pdf','doc','docx']
        ext = ext.strip().lower()
        if ext in formatos:
            self._extensao = ext
        else:
            raise TypeError("Tipo de extensão não suportada")

    @property
    def nome_completo(self):
        return f"'{self.nome}.{self.extensao}'({self.tamanho/1000000}mb)"

class PDF(Arquivo):
    def __init__(self, nome, tam):
        super().__init__(nome, "pdf", tam)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")

class DOC(Arquivo):
    def __init__(self, nome, tam):
        super().__init__(nome, "doc", tam)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word") 