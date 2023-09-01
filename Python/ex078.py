valores = []
for p in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {p}: ')))
    if p == 0:
        menor = maior = valores[p]
    else:
        if valores[p] > maior:
            maior = valores[p]
        elif valores[p] < menor:
            menor = valores[p]
print(f'Você digitou os valores {valores}')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for pos in range(0, 5):
    if menor == valores[pos]:
        print(f'{pos}... ', end='')
print(f'\nO maior valor digitado foi {maior} nas posições ', end='')
for pos in range(0, 5):
    if maior == valores[pos]:
        print(f'{pos}... ', end='')
        