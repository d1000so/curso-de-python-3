print('    Gerador de PA    ')
print('-=-' * 7)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
count = 0
while count != 10:
    print(f'{termo} >', end=' ')
    termo += razao
    count += 1
count2 = 0
print('PAUSA')
n = int(input('Quer mostrar a mais quantos? '))
while n != 0:
    print(f'{termo} >', end=' ')
    termo += razao
    count2 += 1
    count += 1
    if count2 == n:
        print('PAUSA')
        count2 = 0
        n = int(input('Quer mostrar a mais quantos? '))
                
print(f'Progressão finalizada com {count} termosmostrados.')
