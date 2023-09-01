print(f'{"LISTAGEM DE PREÇOS":^40}')
print('.' * 40 + '\n')
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,  'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for i, j in enumerate(lista):
    if i % 2 == 0:
        print(f'{j:.<31}R$', end='')
    else:
        print(f'{j:>7.2f}\n')
    