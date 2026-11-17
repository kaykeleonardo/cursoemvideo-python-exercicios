class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self._titular = nome
        self.__saldo = saldo
        print(f"Conta {self.id} criada com sucesso._Titularidade de {self._titular} com saldo de R${self.__saldo:,.2f}")

    def __str__(self):
        #return f'O saldo da conta {self.id} do cliente {self._titular} possui de R${self.__saldo:,.2f} de saldo.'
        return f"Estado atual da conta: {self.__dict__}"

    def depositar(self, valor):
        self.__saldo += abs(valor)
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}.")

    def sacar(self,valor):
        if valor > self.__saldo:
            print(f"Saque \033[031mNEGADO\033[m no valor de R${valor:,.2f} na conta {self.id}.\nMotivo: \033[031mSALDO INSUFICIENTE\033[m")
        else:
            self.__saldo -= abs(valor)
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}.")




