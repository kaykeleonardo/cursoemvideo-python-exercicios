km = float(input('Digite quantos km tem sua viagem: '))
if  0 < km <= 200 :
    preco = 0.50 * km
    print(f'Você pagara R${preco:.2f} na sua viagem!')
elif km > 200:
    preco = 0.45 * km
    print(f'Você pagara R${preco:.2f} na sua viagem!')
elif km <= 0:
    print('Erro, tente novamente!')