fator = int(input('''Digite um número para
calcular seu fatorial: '''))
indice = fator
print(f'Calculando {fator}! = {fator}', end=' ')
while indice != 1:
    indice -= 1
    fator *= indice
    print(f'x {indice}', end=' ')
print(f'= {fator}')
    