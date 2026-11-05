import datetime
maior = 0
menor = 0
ano = datetime.datetime.now().year
for x in range(0,7):
    nasc = int(input(f'Digite o ano de nascimento da pessoa {x + 1}: '))
    idade = ano - nasc
    if idade < 21:
        menor = menor + 1
    else:
        maior = maior + 1
print(f'''Quantidade de menores de idade = {menor}
Quantidade de maiores de idade = {maior}''')
