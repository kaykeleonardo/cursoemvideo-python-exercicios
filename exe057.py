sex = input('Digite o sexo [M/F]: ').upper().strip()[0]

while sex != 'M' and sex != 'F':
# Pode ser tambem -> while sex not in 'MF':
    sex = input('Sexo invalido, digite o sexo novamente [M/F]: ').upper().strip()[0]
if sex == 'M':
    print('Sexo masculino')
if sex == 'F':
    print('Sexo feminino')

