times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
         'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco',
         'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude',
         'RB Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')
print(f'Tabela {times}')
print('-=' * 20)
print(f'Os 5 primeiros colocados do Brasileirão 2024 foram {times [0:5]}')
print('-=' * 20)
print(f'Os 4 ultimos são {times[16:len(times)]}')
print('-=' * 20)
print(f'Times em ordem alfabetica {sorted(times)}')
print('-=' * 20)
print(f'O vasco esta na {times.index('Vasco') + 1}ª posição')
