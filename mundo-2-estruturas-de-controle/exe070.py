name = barato = ''
price = total = mil = menor = cont = 0
while True:
    name = input('Digite o nome do produto: ')
    price = float(input('Digite o preço do produto: $'))
    total += price
    cont += 1
    if cont == 1:
        barato = name
        menor = price
    elif menor > price:
        menor = price
        barato = name
    if price > 1000:
        mil += 1
    go = input('Deseja continuar [S/N]: ').strip().upper()[0]
    if go == 'N':
        break
print(f'''
O produto mais barato é {barato}
Quantidade de produtos que custa mais de mil: {mil}
Total gasto na compra = ${total}''')

