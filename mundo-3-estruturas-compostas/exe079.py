numeros = []
valor = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor in numeros:
        print('Valor ja existente na lista')
    else:
        numeros.append(valor)
        print('Valor adicionado')
    resposta = input('Deseja continuar [S/N] ? ').upper()
    if resposta in 'N':
        break
print('=-' * 40)
print(numeros)
numeros.sort()
print(numeros)