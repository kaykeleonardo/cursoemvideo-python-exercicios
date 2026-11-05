n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print(f'O maior é {n1}, e o menor é {n3}')
        else:
            print(f'O maior é {n1}, e o menor é {n2}')
    else:
        print(f'O maior é {n3}, e o menor é {n2}')
elif n2 > n3:
    if n3 > n1:
        print(f'O maior é {n2}, e o menor é {n1}')
    else:
        print(f'O maior é {n2}, e o menor é {n3}')
else:
    print(f'O maior é {n3}, e o menor é {n1}')
