import random

lista = []
dados = []
jogos = int(input('Quantos jogos serao feitos ? '))
for cont in range(0,jogos):
    for x in range(0,6):
        n = random.randint(0,60)
        dados.append(n)
    lista.append(dados[:])
    dados.clear()
print('=-' * 5, f'SORTEANDO {jogos} JOGOS', '=-' * 5)
for y in range(0,jogos):
    print(f'Jogo {y+1}: ',lista[y])