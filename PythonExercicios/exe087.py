matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = 0
coluna_tres = 0
linha_dois = 0
for x in range(0,3):
    for p in range(0,3):
        matriz[x][p] = int(input(f'Digite um valor para a posição [{x},{p}]: '))
        if matriz[x][p] % 2 == 0:
            soma += matriz[x][p]
        if p == 2:
            coluna_tres += matriz[x][p]
for x in range(0,3):
    for p in range(0,3):
        print(f'[{matriz[x][p]}]', end='')
    print()
print('=-' * 40)
print(f'A soma dos valores é : {soma}')
print(f'A soma dos valores da terceira coluna é : {coluna_tres}')
print(f'A soma dos valores da segunda linha é : {max(matriz[1])}')