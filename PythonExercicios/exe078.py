numeros = []
for v in range(0,5):
    numeros.append(int(input(f'Digite um valor para a posição {v}: ')))
print('=-' * 40)
print(f'Você digitou os valores: {numeros}')
for c, v in enumerate(numeros):
    if v == max(numeros):
        posicao_maior = c
    if v == min(numeros):
        posicao_menor = c
print(f'Maior valor {max(numeros)} na posição {posicao_maior}')
print(f'Menor valor {min(numeros)} na posição {posicao_menor}')
