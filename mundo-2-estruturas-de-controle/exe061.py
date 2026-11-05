n = int(input('Numero '))
r = int(input('Razao '))
cont = 0
while cont < 10:
    print(f'{n}',' -> 'if cont < 9 else '-> Acabou', end='')
    n += r
    cont +=1
