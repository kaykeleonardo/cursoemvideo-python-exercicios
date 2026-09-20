soma = 0
cont = 0
maioridade = 0
nomehomem = ''
for x in range(1,5):
    nome = input(f'Digite o nome da {x}ª pessoa: ')
    idade = int(input(f'Digite a idade da {x}ª pessoa: '))
    sexo = input(f'Digite o sexo da {x}ª pessoa M/F: ')
    soma += idade
    if x == 1 and sexo in 'Mm':
        maioridade = idade
        nomehomem = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomehomem = nome
    if sexo in 'Ff':
        if idade > 20:
            cont = cont + 1
media = soma / 4
print(f'''Nome do homem mais velho = {nomehomem}
Media de idade = {media}
Mulheres com mais de 20 = {cont}''')