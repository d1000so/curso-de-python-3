numbers = (int(input('Digite um valor: ')),
int(input('Digite um valor: ')),
int(input('Digite um valor: ')),
int(input('Digite um valor: ')))
nove = numbers.count(9)
print(f'Você digitou os valores: {numbers}')
print(f'O valor 9 apareceu {nove} vezes')
if 3 in numbers:
    print(f'O valor 3 apareceu na {numbers.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não aparece nos números')
print(f'Oa valores pares digitados foram ', end=' ')
for i in numbers:
    if i % 2 == 0:
        print(i)
