count = 0
soma = 0
for m in range(1, 500, 2):
    if m % 3 == 0:
        count += 1
        soma += m
print(f'A soma de todos os {count} valores solicitados é {soma}')
