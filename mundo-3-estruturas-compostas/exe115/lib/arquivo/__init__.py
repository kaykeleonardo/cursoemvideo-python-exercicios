from lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        print(f"\033[031mArquivo não encontrado, Criando arquivo\033[m")
        criarArquivo(nome)


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print(f"\033[031mErro: Não foi possivel criar o arquivo.\033[m")
    else:
        print(f"Arquivo {nome} foi criado com sucesso")


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print(f"\033[031mErro ao ler arquivo\033[m")
    else:
        cabecalho("Pessoas Cadastradas")
        for line in a:
            dado = line.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
        print(linha())
    finally:
        a.close()
        input(f"\033[90mAperte algum botão para continuar...\033[m ")


def cadastrarPessoa(arq, nome, idade):
    try:
        a = open(arq, "at")
        a.write(f"{nome};{idade}\n")
    except:
        print(f"\033[031mOcorreu um erro ao cadastrar a pessoa.\033[m")
    else:
        print(f"\033[033mPessoa cadastrada com sucesso.\033[m")
    finally:
        a.close()
        print(linha())
        input(f"\033[90mAperte algum botão para continuar...\033[m ")


def limparLista(nome):
    try:
        a = open(nome, "wt")
    except:
        print(f"\033[031mOcorreu um erro ao limpar a lista.\033[m")
    else:
        a.close()
        cabecalho("A lista foi limpa.")
        input(f"\033[90mAperte algum botão para continuar...\033[m ")
