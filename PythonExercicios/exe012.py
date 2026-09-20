preco = float(input('Digite o preço do produto: '))
desconto = preco - (preco * 5/100)
print(f'O produto que custa R${preco} tera o desconto de 5% e ficara no preço de R${desconto:.2f}')