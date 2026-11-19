from hashlib import sha256
from rich import print, inspect
from pwinput import pwinput

class ContaBancaria:
    def __init__(self, id:int, nome:str = None, saldo:float = 0.0, senha:str = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if senha is None:
            senha = self.pede_senha()
        self.__hash = sha256(senha.encode('utf-8')).hexdigest()
        print("Conta criada com sucesso")

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome:str):
        senha = self.pede_senha()
        if self.validar_senha(senha):
            if not isinstance(nome,str):
                raise TypeError("O nome deve ser um texto")
            if not nome.strip().replace(" ","").isalpha():
                raise ValueError("O nome so pode conter letras")
            self._titular = nome.strip()
        else:
            print("Não foi possivel alterar o nome!")

    def validar_senha(self, chave:str):
        criptografada = sha256(chave.encode('utf-8')).hexdigest()
        if criptografada == self.__hash:
            print("Autorizado")
            return True
        else:
            print("Senha Invalida")
            return False

    def pede_senha(self):
        senha = pwinput()
        return senha

    def sacar(self, valor, chave:str = None):
        if chave is None:
            chave = self.pede_senha()
        if self.validar_senha(chave) and isinstance(valor, (int,float)) and valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print("Saque realizado")
            else:
                print("Saldo insuficiente")
        else:
            print("Não foi possivel realizar o saque!")

    def depositar(self, valor):
        if isinstance(valor, (int,float)) and valor > 0:
            self.__saldo += valor
            print(f"Deposito no valor de {valor} realizado.")
        else:
            print("Valor para deposito invalido!")
