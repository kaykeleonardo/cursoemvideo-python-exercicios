n = int(input('Numero '))
r = int(input('Razao '))
decimo = n + (10-1) * r
for c in range(n,decimo, r):
    print(c,'->', end=' ' )
print('Acabou')
