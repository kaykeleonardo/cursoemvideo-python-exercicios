numeros = []
maior = 0
menor = 0

for v in range(0,5):
    numeros.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v == 0:
        maior = v
        menor = v
    elif numeros[v] > maior:
        maior = v
    elif numeros[v] < menor:
        menor = v    

print('=-' * 40)
print(f'Você digitou os valores: {numeros}')

for c, v in enumerate(numeros):
    if c == 0:
        maior = v
        menor = v
    elif v > maior:
        maior = v
    elif v < menor:
        menor = v

print(f'O maior valor é {maior} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
         print(f'{i}... ', end='')

print(f'\nO menor valor é {menor} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
         print(f'{i}... ', end='')