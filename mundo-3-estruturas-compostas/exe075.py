nove = 0

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o quarto numero: '))

numeros = (n1, n2, n3, n4)

print(f'O nove apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro 3 esta na posição {numeros.index(3) + 1}')
else:
    print('O valor 3 não foi digitado.')
print(f'Valores pares digitados: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
