import math
angulo = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'Valor do seno = {seno:.2f} \n'
      f'Valor do coseno {coseno:.2f}\n'
      f'Valor da tangente {tangente:.2f}')