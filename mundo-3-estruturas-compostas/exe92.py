from datetime import date
dados = dict()

dados['Nome'] = input("Nome: ")
anoNascimento = int(input("Ano de Nascimento: ")) 
dados['Idade'] =  date.today().year - anoNascimento
dados['Ctps'] = int(input("Carteira de Trabalho: "))

if dados['Ctps'] != '0':
    dados['Contratação'] = int(input("Ano Contrataçao: "))
    dados['Salário'] = float(input("Valor Salario: "))
    dados['Aposentadoria'] = dados['Contratação'] + 35 - anoNascimento

print('-=' * 30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
