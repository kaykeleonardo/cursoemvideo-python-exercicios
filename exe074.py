import random
numeros = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
print(f'Valores sorteados : ', end='')
for n in numeros:
    print(n, end=' ')
print(f'\nMaior valor: {max(numeros)}')
print(f'Menor valor: {min(numeros)}')