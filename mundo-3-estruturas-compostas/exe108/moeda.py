def aumentar(valor, porcentagem):
    return valor + (valor * (porcentagem / 100))
    

def diminuir(valor, porcentagem):
    return valor - (valor * (porcentagem / 100))
    

def dobro(valor):
    return valor * 2
    

def metade(valor):
    return valor / 2

def moeda(valor):
    valor = f'{valor:.2f}'
    txt = 'R$' + str(valor).replace('.', ',')
    return txt    