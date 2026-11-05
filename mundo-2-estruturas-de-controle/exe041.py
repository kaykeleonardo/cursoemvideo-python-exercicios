from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc

if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Junior')
elif 19 < idade <= 20:
    print('Senior')
else:
    print('Master')