n = int(input('Digite um numero: '))
tot = 0
for c in range(1 ,n+1):
    if n % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[33m', end='')
    print(c, end=' ')
print('\033[m'f'\nO numero {n} foi divisivel {tot} vezes.')
if tot <= 2:
    print('\033[32m'f'O numero {n} é primo')
else:
    print('\033[31m'f'O numero {n} não é primo')