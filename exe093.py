jogador = {}
gols = []
total = 0

jogador["Nome"] = input("Nome do Jogador: ")
qtdPartidas = int(input(f"Quantidade partidas {jogador['Nome']} jogou ?"))

for x in range(qtdPartidas):
    n = int(input(f"Gols na partida {x + 1}: "))
    gols.append(n)
    total += n

jogador["Gols"] = gols
jogador["Total"] = total

print("-=" * 30)
print(jogador)
print("-=" * 30)

for k, v in jogador.items():
    print(f"{k} tem o valor {v}")

print("-=" * 30)
print(f'O jogador {jogador["Nome"]} jogou {qtdPartidas} partidas')

for i, x in enumerate(gols):
    print(f"Na partida {i + 1}, fez {x} gols.")

print(f"Foi um total de {total} gols")
