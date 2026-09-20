ask = ''
maior = menor =  media = None
cont = 0
soma = 0
n = 0
while ask != 'N':
        n = int(input('Digite um numero '))
        cont += 1
        soma += n
        if cont == 1:
            maior = n
            menor = n
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        ask = input('Deseja continuar [Y/N] ? ').strip().upper()[0]

media = soma / cont
print('Finish...')
print(f'''Quantidade de numero digitados {cont}
Maior numero: {maior}
Menor numero: {menor}
Media dos numeros: {media}''')




