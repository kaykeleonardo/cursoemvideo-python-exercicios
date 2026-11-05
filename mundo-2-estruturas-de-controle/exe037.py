n = int(input('Digite um numero: '))
base = str(input('''Qual base você deseja converter:
1 - Binario
2 - Octal
3 - Hexadecimal
R: '''))
if base == '1':
    print(f'O numero {n} em binario é {bin(n)}')
elif base == '2':
    print(f'O numero {n} em octal é {oct(n)}')
elif base == '3':
    print(f'O numero {n} em hexadecimal é {hex(n)}')
else:
    print('Base digitada invalida')