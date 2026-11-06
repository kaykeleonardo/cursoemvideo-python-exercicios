def leiaDinheiro(msg):
    valido = False
    while valido == False:
        x = str(input(msg)).replace(',', '.').strip()
        if x.isalpha() or x == '':
            print("Valor Invalido")
        else:
            valido = True
    return float(x)