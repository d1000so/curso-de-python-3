print('    Gerador de PA    ')
print('-=-' * 7)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + razao, razao):
    print(f'{i}', end=' > ')
print('fim')2
