n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print(f'O maior numero é {n1}')
elif n2 > n1:
    print(f'O maior numero é {n2}')
else:
    print('Ambos numeros sao iguais')