t = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
               'Flamengo', 'Athletico PR', 'Atlético MG', 'Fortaleza',
               'São Paulo', 'América MG', 'Botafogo', 'Santos', 'Goiás',
               'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético GO',
               'Avaí', 'Juventude')

print('-=' * 20 + '-')
print(f'Os 5 primeiros são: {t[0:5]}')
print('-=' * 20 + '-')
print(f'Os últimos 4 são: {t[-4:]}')
print('-=' * 20 + '-')
print(f'Times em ordem alfabética: {sorted(t)}')
print('-=' * 20 + '-')
p = 'Palmeiras'
print(f'{p} está na posição: {t.index(p) + 1}')