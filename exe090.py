escola = dict()

escola['Nome'] = str(input("Nome: "))
escola['Nota'] = float(input(f'Média de {escola['Nome']}: '))
if escola['Nota'] >= 6:
    escola['Situacao'] = 'Aprovado'
else:
    escola['Situacao'] = 'Reprovado'

print(f'''Nome é igual a {escola['Nome']}
Média é igual a {escola['Nota']}
Situação é igual a {escola['Situacao']}''')


