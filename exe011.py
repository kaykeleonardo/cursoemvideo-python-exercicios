largura = float(input('Digite a largura da sua parede em m: '))
altura = float(input('Digite a altura da sua parede em m: '))
mq = largura * altura
tinta = 0.5 * mq
print(f'Sua parede tem dimensao de {largura}x{altura} e sua área é de {mq}m²')
print(f'Para pintar a parede você ira precisa de {tinta}l de tinta')