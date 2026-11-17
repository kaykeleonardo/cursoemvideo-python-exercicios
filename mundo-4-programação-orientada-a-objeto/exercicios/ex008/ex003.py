class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Titularidade de {self.titular} com saldo de R${self.saldo:,.2f}")

    def __str__(self):
        return f'O saldo da conta {self.id} do cliente {self.titular} possui de R${self.saldo:,.2f} de saldo.'

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}.")

    def sacar(self,valor):
        if valor > self.saldo:
            print(f"Saque \033[031mNEGADO\033[m no valor de R${valor:,.2f} na conta {self.id}.\nMotivo: \033[031mSALDO INSUFICIENTE\033[m")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}.")


c1 = ContaBancaria(112,'Joseph',3000.0)
c1.sacar(4000)
c1.depositar(1000)
print(c1)

