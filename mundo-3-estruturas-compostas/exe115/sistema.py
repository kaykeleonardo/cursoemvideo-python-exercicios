from lib.interface import *
from lib.arquivo import *
from time import sleep

nomeArquivo = "arqsistema.txt"
arquivoExiste(nomeArquivo)


while True:
    limparConsole()
    resposta = menu(
        ["Listar Pessoas", "Cadastrar Pessoa", "Limpar Lista", "Sair do Programa"]
    )
    if resposta == 1:
        limparConsole()
        lerArquivo(nomeArquivo)
    elif resposta == 2:
        limparConsole()
        cabecalho("Novo Cadastro")
        try:
            nome = str(input("Nome: "))
            idade = int(input("Idade: "))
        except ValueError:
            print("Erro: Valor digitado inválido...")
        except Exception as erro:
            print(f"Erro: {erro}")
        else:
            cadastrarPessoa(nomeArquivo, nome, idade)
    elif resposta == 3:
        limparLista(nomeArquivo)
    elif resposta == 4:
        cabecalho("Saindo do Programa...")
        break
    else:
        cabecalho("Erro: Valor Invalido")
    sleep(0.3)
