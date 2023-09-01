print('    Gerador de PA    ')
print('-=-' * 7)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
count = 0
while count != 10:
    print(f'{primeiro} >', end=' ')
    primeiro += razao
    count += 1
print('fim')
