tupla = ('vasco', 'mouse', 'galo', 'teste', 'rampa', 'tesoura', 'celic', 'teclado')
for p in tupla:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
