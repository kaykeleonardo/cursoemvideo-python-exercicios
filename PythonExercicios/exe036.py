casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o salario do comprador: '))
ano = int(input('Em quantos anos ira ser pago o imovel: '))

limite_salario = salario * 30 / 100
meses = ano * 12
parcela = casa / meses
if parcela > limite_salario:
    print('Você não podera comprar essa casa!')
else:
    print(f'Você podera comprar o imovêl no valor de R${casa:.2f} , com parcelas de '
          f'R${parcela:.2f} durante {meses} meses')