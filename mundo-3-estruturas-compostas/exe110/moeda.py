def aumentar(valor, porcentagem, format=False):
    valor = valor + (valor * (porcentagem / 100))
    if format:
        valor = moeda(valor)
    return valor
    

def diminuir(valor, porcentagem, format=False):
    valor = valor - (valor * (porcentagem / 100))
    if format:
        valor = moeda(valor)
    return valor    

def dobro(valor, format=False):
    valor *= 2
    if format:
        valor = moeda(valor)
    return valor

def metade(valor, format=False):
    valor /= 2
    if format:
        valor = moeda(valor)
    return valor

def moeda(valor):
    valor = f'{valor:.2f}'
    txt = 'R$' + str(valor).replace('.', ',')
    return txt

def resumo(valor, aumento, reduz):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'''Preço analisado: {moeda(valor)}
Dobro do preço {dobro(valor, True)}
Metade do Preço: {metade(valor, True)}
{aumento}% de aumento: {aumentar(valor, aumento, True)}
{reduz}% de redução: {diminuir(valor, reduz, True)}''')
    print('-' * 30)


