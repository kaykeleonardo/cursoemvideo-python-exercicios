print(45 * '-')
texto = print('''Calculo de multa
Velocidade maxima 80km/h
Valor da multa: R$7,00 por km excedido''')
print(45 * '-')

km = int(input('Digite a velocidade do veiculo: '))
if km>80:
    multa = (km - 80) * 7
    print(f'Você foi multado em R${multa:.2f} !')
else:
    print('Você não foi multado !')
