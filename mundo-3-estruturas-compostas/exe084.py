entrada = []
pessoas = []
mai = men = 0

while True:
    entrada.append(str(input("Nome da Pessoa: ")))
    entrada.append(float(input("Peso da Pessoa: ")))
    if len(pessoas) == 0:
        mai = men = entrada[1]
    else:
        if entrada[1] > mai:
            mai = entrada[1]
        elif entrada[1] < men:
            men = entrada[1]
    pessoas.append(entrada[:])
    entrada.clear()
    flag = input("Deseja continuar ? S/N ")
    if flag in'Nn':
        break

print(f'Quantidade de pessoas cadastradas {len(pessoas)}')
print(f'Menor peso foi de {men}Kg. Peso de ', end='')
for x in pessoas:
    if x[1] == men:
        print(f'[{x[0]}]', end=' ')
print()
print(f'Maior peso foi de {mai}Kg. Peso de ', end='')
for x in pessoas:
    if x[1] == mai:
        print(f'[{x[0]}]', end=' ')
