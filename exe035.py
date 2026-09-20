r1 = float(input('Digite o tamanho da reta 1: '))
r2 = float(input('Digite o tamanho da reta 2: '))
r3 = float(input('Digite o tamanho da reta 3: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('As retas podem formar um triangulo!')
else:
    print('As retas não podem formar um triangulo!')