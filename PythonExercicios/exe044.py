valor = float(input('Digite o valor do produto: '))
pagamento = input('''Qual a forma de pagamento:
1- A vista dinheiro (10% desconto)
2- A vista cartão   (5% desconto)
3- 2x cartão        
4- 3x ou mais cartão (20% Juros)
''')

if pagamento == '1':
    novo = valor - valor * 10/100
    print(f'Sua compra de R${valor} com desconto de 10% ficara R${novo:.2f}')
elif pagamento == '2':
    novo = valor - valor * 5/100
    print(f'Sua compra de R${valor} com desconto de 5% ficara R${novo:.2f}')
elif pagamento == '3':
    print(f'Sua compra de {valor} sera parcelada de 2x sem juros \n'
          f'Os valores das parcelas serão de R${valor / 2:.2f}')
elif pagamento == '4':
    parcelas = int(input('Qual o numero de parcelas: '))
    novo = valor + valor * 20/100
    print(f'Sua compra de {valor} foi dividida em {parcelas}x com 20% de juros \n'
          f'O valor total sera de {novo:.2f} com {parcelas} parcelas de {novo / parcelas:.2f}')
else:
    print('Opção invalida, tente novamente')