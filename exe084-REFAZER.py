galera = list()
dados = list()
pesada = list()
leve = list()
cont_pessoas = 0

while True:
    dados.append(str(input('Nome da pessoa: ')))
    dados.append(int(input('Peso da pessoa: ')))
    galera.append(dados[:])
    dados.clear()
    cont_pessoas += 1
    continuar = input('Deseja continuar [S/N] ? ')
    if continuar in 'Nn':
        break

cont = 0
for x in galera:
    if len(leve) == 0 and len(pesada) == 0:
        pesada.append(x)
        leve.append(x)
        cont += 1
    elif x[1] > pesada[0][1]:
        pesada.clear()
        pesada.append(x)
    elif x[1] < leve[0][1]:
        leve.clear()
        leve.append(x)
    elif x[1] == pesada[0][1]:
        pesada.append(x)
    elif x[1] == leve[0][1]:
        leve.append(x)
print(f'Pessoas adicionadas : {galera}')
print('Pessoas mais leve: ',leve)
print('Pessoas mais pesadas ',pesada)