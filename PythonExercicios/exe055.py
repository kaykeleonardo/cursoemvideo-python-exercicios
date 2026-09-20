menor: 0
maior: 0
for pessoa in range(1,6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'''Maior peso = {maior} 
Menor peso = {menor}''')
