from random import randint as rnd

print('=' * 30)
print(f'   VAMOS JOGAR PAR OU ÍMPAR')
vitoria = resultado = 0
while True:
    opcao = ' '
    print('=' * 30)
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    jogador = int(input('Digite um número? '))
    computador = rnd(0, 10)
    total = jogador + computador
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print('-' * 30)
    print(f' Você jogou {jogador} o computador {computador}')
    print(f'\n    Total de {total} deu {resultado}!\n')
    if opcao == 'P':
        if total % 2 == 0:
            print('  :)  ' * 5)
            print('\n         VOCÊ VENCEU!')
            vitoria += 1
            opcao
        else:
            print('  :(  ' * 5)
            print('\n         VOCÊ PERDEU!')
            break
    elif opcao == 'I':
        if total % 2 != 0:
            print('  :)  ' * 5)
            print('\n         VOCÊ VENCEU!')
            vitoria += 1
        else:
            print('  :(  ' * 5)
            print('\n         VOCÊ PERDEU!')
            break
    print('\n   Vamos jogar novamente...')
print('~' * 30)
print(f'Game Over! Jogadas vencidas {vitoria}')
