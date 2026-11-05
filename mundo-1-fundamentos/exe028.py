import random

n = random.randint(0,5)
descubra = int(input('Digite um numero entre 0 a 5: '))
if descubra == n:
    print('Parabéns, você acertou o numero e venceu!')
else:
    print(f'Você perdeu. O numero era {n}, tente novamente.')

