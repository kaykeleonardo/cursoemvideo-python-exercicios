nome = input('Digite uma frase: ').upper()
print(f'A letra "A" aparece {nome.count('A')} vezes')
print(f'O primeiro "a" aparece na posição {nome.find('A') + 1}')
print(f'O ultimo "A" aparece na posição {nome.rfind('A')}')
