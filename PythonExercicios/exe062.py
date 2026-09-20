n = int(input('Numero '))
r = int(input('Razao '))
decimo = n + (10-1) * r
cont = 0
ntermos = 10
while cont < ntermos :
    print(f'{n}',' -> 'if cont < (ntermos - 1) else ' -> PAUSA', end='')
    n += r
    cont +=1
print()
ntermos = int(input('Quantos termos deseja mostrar a mais: '))
if ntermos <= 0:
    print('Acabou')
else:
    cont = 0
    while cont < ntermos :
        print(f'{n}',' -> 'if cont < (ntermos-1) else '', end='')
        n += r
        cont +=1
