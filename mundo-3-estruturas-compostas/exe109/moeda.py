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