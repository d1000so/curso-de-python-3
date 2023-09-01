num = int(input('Digite um número: '))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
        print(f'\033[1;31m{i}\033[m', end=' ')
    else:
        print(i, end=' ')
print(f'\nO número {num} foi divisível {count} vezes.')
if count == 2:
    print('Portanto, ele É UM NÚMERO PRIMO!')
else:
    print('Portanto, ele NÃO É UM NÚMERO PRIMO!')