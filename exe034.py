salario = float(input('Digite seu salario: '))
if salario > 1250:
    novo = salario + (salario * 10/100)
    print(f'Com aumento de 10% seu salario sera de {novo}')
else:
    novo = salario + (salario * 15/100)
    print(f'Com aumento de 15% seu salario sera de {novo}')