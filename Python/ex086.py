matriz = []
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
    print()
