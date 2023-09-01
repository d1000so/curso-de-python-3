valores = []
opção = ' '
while not opção in 'SN':
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(valor)
    while True:
        opção = input('Quer continuar? [S/N] ').strip().upper()[0]
        if opção == 'S':
            opção = ' '
            break
        elif opção == 'N':
            break
print('=-' * 20)
valores.sort()
print(f'Você digitou os valores {valores}')
