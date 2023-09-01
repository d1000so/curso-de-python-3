from random import randint as rdm
from time import sleep
num = []
print('-' * 47)
print(f'{"Sorteio da Mega Sena":^47}')
print('-' * 47)
sort = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 6+f' < SORTEANDO{sort + 1:^4}JOGOS > '+'=-' * 6)
for s in range(0, sort):
    num.insert(s, [])
    for n in range(0, 6):
        num[s].append(rdm(1, 60))
        num[s].sort()
    sleep(0.5)
    print(f'Jogo {s + 1:>2}: {num[s]}')
sleep(0.5)
print('-=' * 8 + f'{" < BOA SORTE! > "}' + '=-' * 8)