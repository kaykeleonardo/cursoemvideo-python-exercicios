r1 = float(input('Digite o tamanho da reta 1: '))
r2 = float(input('Digite o tamanho da reta 2: '))
r3 = float(input('Digite o tamanho da reta 3: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('As retas podem formar um triangulo ', end='')
    if r1 == r2 == r3:
        print('equilatero')
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print('isoceles')
    else:
        print('escaleno')
else:
    print('Não pode se formar um triangulo')