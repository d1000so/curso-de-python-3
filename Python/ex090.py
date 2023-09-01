aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().title()
while True:
    try:
        aluno['média'] = float(input(f'Média do {aluno["nome"]}: '))
        break
    except:
        print('Ops! O valor digitado não é um número!')
if aluno['média'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 7 > aluno['média'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
    