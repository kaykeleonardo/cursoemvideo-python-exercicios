matriz = [[0,0,0], [0,1,0], [0,0,0]]
for x in range(0,3):
    for p in range(0,3):
        matriz[x][p] = int(input(f'Digite um valor para a posição [{x},{p}]: '))
for x in range(0,3):
    for p in range(0,3):
        print(f'[{matriz[x][p]}]', end='')
    print()
