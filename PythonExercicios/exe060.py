from math import factorial

n1 = int(input('Digite um numero: '))
fatorial = factorial(n1)
while n1 > 0:
    print(f'{n1} ', end='')
    print('x ' if n1 > 1 else '=', end='')
    n1 -= 1
print('',fatorial)

