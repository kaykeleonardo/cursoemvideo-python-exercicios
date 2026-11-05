from math import factorial


def fatorial_auto(n, show=False):
    """
    -> Função para calcular o fatorial
    :param n: Numero ao qual sera calculado o fatorial
    :param show: Definição se ira mostrar o calculo ou não
    :return: valor total
    
    """
    total = factorial(n)
    if show:
        print(f"{n} ", end="")
        for x in range(n, 1, -1):
            print(f"x {x - 1} ", end="")
        print("= ", end="")
    return total


def fatorial_manual(n, show=False):
    f = 1
    for x in range(n, 0, -1):
        if show:
            print(x, end="")
            if x > 1:
                print(' x ', end="")
            else:
                print(' = ', end="")
        f *= x
    return f

help(fatorial_auto)
print(fatorial_auto(5, show=True))
print(fatorial_manual(5, show=False))