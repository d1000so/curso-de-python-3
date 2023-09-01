# Fibonacci series:
# the sum of two elements defines the next
print('-' * 36)
print('       Sequência de Fibonacci       ')
print('-' * 36)
termo = int(input('Quantos termos você quer mostrar? '))
a, b = 0, 1
count = 0
while count != termo:
    print(f'{a} > ', end='')
    a, b = b, a+b
    count += 1
print('fim')