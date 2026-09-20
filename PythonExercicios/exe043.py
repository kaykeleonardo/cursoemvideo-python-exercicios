import math

altura = float(input('Digite sua altura: (m) '))
peso = float(input('Digite seu peso: (Kg) '))
imc = peso / math.pow(altura, 2)

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('obesidade')
else:
    print('Obesidade morbida')