n = int(input('Numero '))
r = int(input('Razao '))
decimo = n + (10-1) * r
cont = 0
while cont < 10:
    print(f'{n}',' -> 'if cont < 9 else '', end='')
    n += r
    cont +=1
