from random import randint as rnd
from time import sleep

enum = 'Vou pensar em um número entre 0 e 10. Tente advinhar...'
print('\033[1;33m-=-' * 19)
print(f'\033[1;34m{enum:^57}')
print('\033[1;33m-=-' * 19)
pensando = rnd(0, 10)
print('\033[1;37mEm que número estou pensando?', end='\033[1;32m ')
acertou = False
count = 0
while not acertou:
    count += 1
    sleep(1)
    num = int(input())
    if pensando > num:
        print(f'\033[1;31m\nMais... Tente mais uma vez!', end=' ')
    elif pensando < num:
        print(f'\033[1;31m\nMenos...Continue tentendo!', end=' ')
    else:
        acertou = True
        print(f'\033[1;32m\nVocê acertou com {count} tentativas. Parabéns!')
print(f'{100 // count} Pontos')