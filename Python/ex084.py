pessoas = []
dados = []
resposta = ' '
maior = menor = 0
while resposta not in 'N':
    dados.append(input('Nome: ').title())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while True:
        resposta = input('Quer Continuar? [S/N] ').strip().upper()[0]
        if resposta in 'S':
            break
        elif resposta in 'N':
            break
print('=-' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O menor peso foi de {menor:.1f}kg, peso de', end='')
for p in pessoas:
    if p[1] == menor:
        print(f' {p[0]}', end=' ...')
print()
print(f'O maior peso foi de {maior:.1f}kg, peso de', end='')
for p in pessoas:
    if p[1] == maior:
        print(f' {p[0]}', end=' ...')
