numeros = [[],[]]
valor = 0
for n in range(0,7):
    valor = (int(input('Digite um numero: ')))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
print(f'Ordem de numeros pares digitados : {numeros[0]}')
numeros[1].sort()
print(f'Ordem dos numeros impares digitados: {numeros[1]}')
