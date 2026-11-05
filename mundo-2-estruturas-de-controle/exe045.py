import random

itens = ('Pedra', 'Papel' , 'Tesoura')
nome = input('Digite seu nome: ')
print()
jogador = int(input(f'''{nome} escolha o que ira jogar:
[0] Pedra
[1] Papel
[2] Tesoura
'''))

cpu = random.randint(0,2)
print()
print(20 * '-=')
if (jogador == 0 and cpu == 2) or (jogador == 1 and cpu == 0) or (jogador == 2 and cpu == 1):
    print(f'{nome}: {itens[jogador]} X {itens[cpu]} :Maquina')
    print(f'{nome} Venceu')
elif (jogador == 1 and cpu == 1) or (jogador == 2 and cpu == 2) or (jogador == 0 and cpu == 0):
    print(f'{nome}: {itens[jogador]} X {itens[cpu]} :Maquina')
    print('Empate')
elif (jogador == 2 and cpu == 0) or (jogador == 0 and cpu == 1) or (jogador == 1 and cpu == 2):
    print(f'{nome}: {itens[jogador]} X {itens[cpu]} :Maquina')
    print('A maquina ganhou')
else:
    print('Resposta invalida')
print(20 * '-=')