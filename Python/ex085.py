num = [[],[]]
valor = 0
for v in range(0, 7):
    valor = int(input(f'Digite o {v + 1}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=-' * 25)
num[0].sort()
print(f'Os valores pares digitados foram: {num[0]}')
num[1].sort()
print(f'Os valores impares digitados foram: {num[1]}')
