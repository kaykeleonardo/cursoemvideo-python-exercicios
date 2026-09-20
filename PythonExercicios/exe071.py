nota50 = nota20 = nota10 = moeda = valor = 0
while True:
    valor = int(input('Digite o valor a ser sacado: '))
    if valor >= 50:
        nota50 = valor // 50
        valor -= nota50 * 50
    if valor >= 20:
        nota20 = valor // 20
        valor -= nota20 * 20
    if valor >= 10:
        nota10 = valor // 10
        valor -= nota10 * 10
    if valor >= 1:
        moeda = valor // 1
        valor -= moeda * 1
    if valor == 0:
        break
print(f'''
Serao sacadas:
{nota50} notas de 50
{nota20} notas de 20
{nota10} notas de 10
{moeda} moedas de 1''')