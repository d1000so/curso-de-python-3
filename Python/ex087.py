matriz = []
pares = terceira = maior = 0
lin = int(input('Quantas linhas tem a matriz? '))
col = int(input('Quantas colunas tem a matriz? '))
for l in range(0, lin):
    matriz.append([])
    for c in range(0, col):
        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l].insert(c, valor)
print('=-' * 20)
for l in range(0, lin):
    for c in range(0, col):
        print(f'[{matriz[l][c]:^5}] ', end='')
        if c == 1 and matriz[l][c] > maior:
            maior = matriz[l][c]
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            terceira += matriz[l][c]
    print()
print('=-' * 20)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'A maior valor da segunda coluna é {maior}')

