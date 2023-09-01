print('Digite PRIMEIRO valor:', end=' ')
v1 = int(input().strip())
print('Digite PRIMEIRO valor:', end=' ')
v2 = int(input().strip())
if v1 > v2:
    print('\nO PRIMEIRO valor é maior.')
elif v1 < v2:
    print('\nO SEGUNDO valor é maior.')
else:
    print('\nOs dois valores são iguais.')