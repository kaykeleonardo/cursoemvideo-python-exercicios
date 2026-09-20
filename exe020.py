import random
nome1 = str(input('Digite o nome do 1º aluno: '))
nome2 = str(input('Digite o nome do 2º aluno: '))
nome3 = str(input('Digite o nome do 3º aluno: '))
nome4 = str(input('Digite o nome do 4º aluno: '))
nomes = [nome1, nome2, nome3, nome4]
random.shuffle(nomes)
print(f'A ordem de apresentação será {nomes}')