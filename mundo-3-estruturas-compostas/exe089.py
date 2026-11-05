lista = []
nomes = []
notas = []
cont = 0
while True:
    nome = input('Digite um nome: ')
    nomes.append(nome)

    n1 = float(input('Digite a primeira nota: '))
    notas.append(n1)
    n2 = float(input('Digite a segunda nota: '))
    notas.append(n2)

    nomes.append(notas[:])
    lista.append(nomes[:])

    nomes.clear()
    notas.clear()

    stop = input('Deseja continuar [S/N] ?').upper()
    if stop in 'N':
        break
print('-' * 15)
for pos in range(0, len(lista)):
    v1 = lista[pos][1][0]
    v2 = lista[pos][1][1]
    media = (v1 + v2) / 2
    print(f'{pos}  {lista[pos][0]} {media}')
print('-' * 15)
while True:
    saber_nota = int(input('A nota de qual aluno você deseja saber (999 interrompe)?'))
    print(f'Notas de {lista[saber_nota][0]} são {lista[saber_nota][1]}')
    if saber_nota == 999:
        break


