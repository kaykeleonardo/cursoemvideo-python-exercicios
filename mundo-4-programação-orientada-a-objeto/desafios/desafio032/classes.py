class ContaBancaria:
    def __init__(self, id, nome, saldo = 0, senha = None):
        self._id = None
        self._titular = None
        self.__saldo = None
        self.__hash = None

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome):
        if not isinstance(nome,str):
            raise TypeError("O nome deve ser um texto")
        if not nome.strip().replace(" ","").isalpha():
            raise ValueError("O nome so pode conter letras")
        
        self._titular = nome.strip()

    def validar_senha(self,chave):
        pass

    def pede_senha(self):
        pass

    def sacar(self, valor, chave):
        pass

    def depositar(self, valor):
        pass
