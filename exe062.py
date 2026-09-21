n = int(input('Numero '))
r = int(input('Razao '))
cont = 0
ntermos = 10
total = ntermos
while cont < ntermos :
    print(f'{n}',' -> 'if cont < (ntermos - 1) else ' -> PAUSA', end='')
    n += r
    cont +=1
while ntermos != 0:

    ntermos = int(input('\nQuantos termos deseja mostrar a mais: '))

    if ntermos <= 0:
        print(f'Finalizado, numeros de termos mostrados = {total}')
    else:
        cont = 0
        while cont < ntermos :
            print(f'{n}',' -> 'if cont < (ntermos-1) else '-> PAUSA', end='')
            n += r
            cont +=1
            total += 1
