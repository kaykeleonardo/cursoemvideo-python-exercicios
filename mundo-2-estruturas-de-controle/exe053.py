txt = input('Digite uma frase/palavra: ').strip().upper()
palavra = txt.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('É um palindromo')
else:
    print('Não é um palindromo')