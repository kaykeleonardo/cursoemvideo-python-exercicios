lista = []
qtde_num = 0
while True:
    lista.append(int(input('Digite um numero para entrar na lista: ')))
    qtde_num += 1
    prosseguir = input('Deseja continuar [S/N] ? ').upper()
    if 'N' in prosseguir:
        break
print('=-' * (len(lista) * 2))
lista.sort()
print(f'Lista digitada {lista}')
print(f'Quantidade de numeros digitados: {qtde_num}')
lista.sort(reverse=True)
print(f'Valores de forma decrescente: {lista}''')
if 5 in lista:
    print('O numero 5 foi digitado')
else:
    print('Numero 5 não foi digitado')

