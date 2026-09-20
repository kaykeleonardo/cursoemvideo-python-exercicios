import random
user = soma = cpu = cont = 0
time = ''
while True:
    user = int(input('Jogue seu numero: '))
    time = input('Você escolhe impar ou par [I/P]').strip().upper()[0]
    cpu = random.randint(0,10)
    soma = user + cpu
    print(f'Você jogou {user} e o computador jogou {cpu}')
    print(f'O numero {soma} é par.' if soma % 2 == 0 else f'O numero {soma} é impar.', end='')
    print()
    if soma % 2 == 0 and time == 'P' or soma % 2 != 0 and time == 'I':
        print('Você venceu!')
        cont +=1
        print()
    else:
        print('Você perdeu!')
        print()
        break
print(f'Jogo finalizado...')
print(f'Vitorias seguidas: {cont}')