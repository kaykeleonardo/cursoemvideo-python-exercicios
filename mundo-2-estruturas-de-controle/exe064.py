n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um numero: '))
    cont += 1
    soma += n
print(f'Acabou, você digitou {cont - 1} numeros, a soma deles foi {soma - 999}')
