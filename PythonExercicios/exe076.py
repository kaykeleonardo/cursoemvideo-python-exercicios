produtos = ('Pão', 1.30, 'Batata', 5.20, 'Picanha', 42, 'Tilapia', 8.50, 'Camarão', 9.90, 'Doritos', 5.65)
print('_' * 40)
print(f'{"Listagem de Preços":^40}')
print('_' * 40)
cont = 0
for item in produtos:
    if cont % 2 == 0:
        print(f'{item:.<30}', end=' ')
    elif cont % 2 != 0:
        print(f'R$ {item:.2f}')
    cont += 1
print('_' * 40)

