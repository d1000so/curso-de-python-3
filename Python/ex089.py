classe = []
aluno = []
con = ' '
print('-' * 33)
print(f'{"Cadastro de Notas":^33}')
print('-' * 33)
while con not in 'N':
    aluno.append(str(input('Nome: ')).strip().title())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 1: ')))
    média = (aluno[1] + aluno[2]) / 2
    aluno.append(média)
    classe.append(aluno[:])
    aluno.clear()
    while True:
        con = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if con == 'S':
            break
        elif con == 'N':
            break
print('-=' * 8 + '-' + '=-' * 8)
print(f'{"Nº":>2}{"ALUNOS":>12}{"MÉDIA":>19}')
print('-' * 33)
for n, a in enumerate(classe):
    print(f'{n:>2}{" ":>6}{a[0]:<20}{a[3]:>5.2f}')
print('-=' * 8 + '-' + '=-' * 8)
con = 0
while con != 999:
    print('\033[1;33mDigite [\033[1;36mN\033[1;33m] do Aluno para ver nota')
    print('\033[1;33mDigite [\033[1;36m999\033[1;33m] para sair: \033[m', end='')
    con = int(input())
    print()
    if con == '999':
        break
    else:
        print(f'As notas de \033[1;36m{classe[con][0]}\033[m são:\n')
        if classe[con][1] < 6:
            print('  Nota 1:\033[1;31m', end=' ')
        else:
            print('  Nota 1:\033[1;32m', end=' ')
        print(f'{classe[con][1]:>5.2f}\033[m', end=' ')
        if classe[con][2] < 6:
            print('| Nota 2:\033[1;31m', end=' ')
        else:
            print('| Nota 2:\033[1;32m', end=' ')
        print(f'{classe[con][2]:>5.2f}\033[m')
        print('-=' * 8 + '-' + '=-' * 8)
print('\033[1;36mAté logo!')
