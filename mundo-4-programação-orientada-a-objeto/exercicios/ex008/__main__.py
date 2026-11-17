from ex003 import *

def main():
    c1 = ContaBancaria(112,'Joseph',3000.0)
    c1.sacar(4000)
    c1.depositar(1000)
    print(c1)


if __name__ == '__main__':
    main()