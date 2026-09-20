sexo = next = ''
idade = maioridade = homem = mulhernova = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()[0]
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulhernova += 1
    next = input('Deseja continuar [S/N]: ').strip().upper()[0]
    print()
    if next == 'N':
        break
print(f''' 
Pessoas com mais de 18: {maioridade}
Quantidade de homens: {homem}
Mulheres com menos de 20: {mulhernova}''')