lista = []
expre = str(input('Digite a expressao: '))

for letra in expre:
    if letra == '(':
        lista.append('(')
    elif letra == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressao valida')
else:
    print('Expressao invalida')