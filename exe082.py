lista = []
par = []
impar = []

while True:
    lista.append(int(input('Digite um numero para colocar na lista: ')))
    seguir = input('Deseja continuar [S/N] ? ').upper()
    if 'N' in seguir:
        break


for x in lista:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
print('=-' * 30)
print(f'Lista padrão completa = {lista}')
print(f'Lista par completa = {par}')
print(f'Lista impar completa = {impar}')


# Foi feita adicionando os itens nas listas posteriormente devido ao pedido do Guanabara, para aprendermos a manipular posteriormente.