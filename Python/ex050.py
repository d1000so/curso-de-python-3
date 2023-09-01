count = 0
soma = 0
for n in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(n)))
    if num % 2 == 0:
        count += 1
        soma += num
print(f'Foram comtados {count} valores pares que somam {soma}')