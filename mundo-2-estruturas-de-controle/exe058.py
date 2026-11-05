import random
chance = 1
n = random.randint(0, 10)

chute = int(input('Tente acertar o numero de 0 a 10: '))

while chute != n:
    chute = int(input('Errou, tente novamente: '))
    chance += 1
print('Parabéns, você acertou!')
print(f'Você precisou de {chance} chances')