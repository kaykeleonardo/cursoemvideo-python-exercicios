n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
''')
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma dos numeros é {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'A multiplicação dos numeros é {mult}')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print('São numeros de mesmo valor')
    elif opcao == 4:
        print('Novos Números')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))

print('Saindo...')

