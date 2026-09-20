numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
                       'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
                       'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input("Digite um numero entre 0 e 20: "))
    if n < 0 or n > 20:
        print("Valor invalido")
    else:
        print(f'Você digitou o numero {numeros[n]}')
        break