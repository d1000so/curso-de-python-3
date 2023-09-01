n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print(f'O aluno(a) tirou as notas {n1} e {n2}, a média é {média:.1f}')
if média < 5:
    print('O aluno está REPROVADO!')
elif média >= 7:
    print('O aluno está de APROVADO!')
else:
    print('O aluno está de RECUPERAÇÃO')