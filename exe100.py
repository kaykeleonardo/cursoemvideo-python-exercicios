from random import randint
from time import sleep


def sorteia(lst):
    print("Valores Presentes na Lista: ", end="", flush=True)
    for x in range(10):
        n = randint(1, 10)
        lst.append(n)
        print(f"{n} ", end="", flush=True)
        sleep(0.4)
    print("PRONTO")


def somaPar(lst):
    soma = 0
    for x in lst:
        if x % 2 == 0:
            soma += x
    print(f"Somando os valores pares de {lst}, temos {soma}")


lista = []
print("-=" * 30)
sorteia(lista)
somaPar(lista)
