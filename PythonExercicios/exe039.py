from datetime import date
nasc = int(input('Qual ano você nasceu: '))
atual = date.today().year
idade = atual - nasc

if idade == 18:
    print('Você precisa se alistar')
elif idade > 18:
    atraso = idade - 18
    print(f'''Você ja deveria ter se alistado á {atraso} anos
Seu alistamento foi em {atual - atraso}''')
else:
    adiantado = 18 - idade
    print(f'Faltam {adiantado} anos pra você se alistar')
    print(f'Seu alistamento sera em {atual + adiantado}')