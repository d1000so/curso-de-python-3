from random import randint as rnd
from time import sleep
from tqdm import tqdm

enum = 'Vou pensar em um número entre 0 e 5. Tente advinhar...'
print('\033[1;33m-=-' * 19)
print('\033[1;34m', enum)
print('\033[1;33m-=-' * 19)
pensando = rnd(0, 5)
print('\033[1;37mEm que número estou pensando?', end='\033[1;32m ')
num = int(input())
print('\nProcessando', end=' ')
for i in tqdm(range(30)):
    sleep(0.1)
if pensando == num:
    print('\033[1;32m\nParabéns! Você advinhou...')
else:
    print(f'\033[1;31m\nGanhei! Eu pensei em {pensando} e não em {num}')
