elenco = []
while True:
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
    elenco.append(jogador)
    while True:
        parada = input("Quer continuar? [S/N] ").upper()[0]
        if parada in "SN":
            break
        print("ERRO! Digite apenas [S/N]")
    if parada == "N":
        break
print("-=" * 30)
print("cod  ", end="")
for i in jogador.keys():
    print(f"{i:<16}", end=" ")
print()
print("-" * 60)
for i, v in enumerate(elenco):
    print(f"{i:<4}", end=" ")
    for d in v.values():
        print(f"{str(d):<15} ", end=" ")
    print()
print("-=" * 30)
while True:
    busca = int(input("Mostrar dados de qual jogador ? (999 para parar) "))
    if busca == 999:
        break
    elif busca >= len(elenco):
        print("Codigo Invalido")
    else:
        print(f"Levantamento do jogador {elenco[busca]["Nome"]}:")
        for i, g in enumerate(elenco[busca]["Gols"]):
            print(f"Na partida {i+1} fez {g} gols")
    print("-=" * 30)
print("-=" * 30)
print("<<<VOLTE SEMPRE>>>")
