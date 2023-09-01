a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

menor = a
if b <= a and b <= c:
    menor = b
if c <= a and c <= b:
    menor = c
print(f'O menor número digitado foi: {menor}')
maior = a
if b >= a and b >= c:
    maior = b
if c >= a and c >= b:
    maior = c
print(f'O maior número digitado foi: {maior}')
