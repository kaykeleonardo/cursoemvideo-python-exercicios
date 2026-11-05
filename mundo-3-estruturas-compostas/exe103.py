def ficha(nome='<desconhecido>', gols='0'):
    return f"O jogador {nome} fez {gols} no campeonato"


n = input("Nome do Jogador: ")
g = (input("Número de Gols: "))

if g.isnumeric():
    g= int(g)
else:
    g = 0
if n.strip() =='':
    print(ficha(gols=g))
else:
    print(ficha(n,g))