peso = 0
peso_min = 0
peso_max = 0
for i in range(1,6):
    peso = float(input('O peso da {}ª pessoa é: '.format(i)))
    if i == 1:
        peso_min = peso
        peso_max = peso
    else:
        if peso_min > peso:
            peso_min = peso
        if peso_max < peso:
            peso_max = peso
print(f'O menor peso lido foi {peso_min}')
print(f'O maior peso lido foi {peso_max}')