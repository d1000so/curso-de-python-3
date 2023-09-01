conta_idade = homem = mulher = 0
while True:
    idade = 0
    sexo = continuar = ' '
    idade = int(input('Idade? '))
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
        if idade >= 18:
            conta_idade += 1
    else:
        if idade < 20:
            if idade >= 18:
                mulher += 1
                conta_idade += 1
            else:
                conta_idade += 1
        else:
            mulher += 1
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Cadastro encerrado...')
print(f'Pessoas maiores cadastradas {conta_idade}')
print(f'Homens cadastrados {homem}')
print(f'Mulheres menores {mulher}')
