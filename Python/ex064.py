n = count = soma = 0
n = int(input('Digite um número [ 999 para parar ]: '))
while n != 999:
    soma += n
    count += 1
    n = int(input('Digite um número [ 999 para parar ]: '))
print(f'Você digitou {count} números e a soma entre eles é {soma}.')
