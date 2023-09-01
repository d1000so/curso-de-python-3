from time import sleep
import os
from random import randint

opções = ['PEDRA', 'PAPEL', 'TESOURA']

os.system('clear')

while True:
    print('''
ESCOLHA SUA ARMA:\n
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA\n''')
    computer = randint(0, 2)
    jogador = int(input('Qual é sua jogada? ').strip())
    if computer == jogador:
        resultado = 'EMPATE'
        break
    elif computer < jogador and jogador <= 2 and (jogador - computer) == 1:
        resultado = 'JOGADOR VENCEU'
        break
    elif jogador < computer and (computer - jogador) == 1:
        resultado = 'COMPUTADOR VENCEU'
        break
    elif jogador - computer == 2 and jogador <= 2:
        resultado = 'COMPUTADOR VENCEU'
        break
    elif computer - jogador == 2:
        resultado = 'JOGADOR VENCEU'
        break
    elif jogador > 2:
        os.system('clear')
        print('### ESCOLHA INVÁLIDA ###')
        sleep(2)
        os.system('clear')

sleep(0.5)
print('JO')
sleep(1)
print('KEN',)
sleep(1)
print('PÔ!!!')
sleep(0.5)
print('-=' * 13, end='-\n')
print(f'O computador jogou {opções[computer]}')
print(f'Você jogou {opções[jogador]}')
print('-=' * 13, end='-\n')
print(resultado)
