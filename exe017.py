import math

oposto = float(input('Qual valor do cateto oposto: '))
adjascente = float(input('Qual valor do cateto adjascente: '))
hipotenusa = math.hypot(oposto, adjascente)
print(f'O valor da hipotenus do triangulo é {hipotenusa:.2f}')