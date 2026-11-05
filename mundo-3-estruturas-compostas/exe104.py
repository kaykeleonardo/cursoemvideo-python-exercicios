def leiaInt(valor):
    ok = False
    string = str(input(valor))
    while ok == False:
        if string.isnumeric():
            valor = int(string)
            ok = True
        else:
            print("Valor Digitado Invalido")
            string = str(input(valor))
        if ok:
            break
    return valor
n = leiaInt("Digite um n: ")
print(f"Valor digitado: {n}")