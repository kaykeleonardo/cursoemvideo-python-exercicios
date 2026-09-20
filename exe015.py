import math

dia = int(input('Quantos dias alugados: '))
km = float(input('Quantos km rodados: '))
preco_km = km * 0.15
preco_dia = dia * 60
print(f'O valor total a pagar é de R${preco_km + preco_dia:.2f}')
