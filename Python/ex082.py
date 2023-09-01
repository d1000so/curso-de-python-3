principal = []
pares = []
impares = []
resposta = ' '
while resposta not in 'N':
    principal.append(int(input('Digite um número: ')))
    if principal[-1] % 2 == 0:
        pares.append(principal[-1])
    else:
        impares.append(principal[-1])
    while True:
        resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resposta in 'S':
            break
        elif resposta in 'N':
            break
print(f'A lista principal é {principal}')
print(f'A lista de pares é {pares}')
print(f'A lista de pares é {impares}')
    