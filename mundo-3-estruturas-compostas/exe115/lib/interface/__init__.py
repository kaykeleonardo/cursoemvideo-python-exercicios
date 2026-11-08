import os


def linha(tam=40):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(f"\033[036m{txt.center(40)}\033[m")
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    for p, val in enumerate(lista):
        print(f"\033[33m{p + 1} \033[m- \033[032m{val}\033[m")
    print(linha())
    resp = leiaInt("Sua Opção: ")
    return resp


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro: por favor, digite um número válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[31mEntrada de dados interrompida pelo usuário.\033[m")
            return 4
        else:
            return n


def limparConsole():
    os.system("cls" if os.name == "nt" else "clear")
