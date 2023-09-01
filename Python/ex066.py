# ex066
count = num = soma = 0
while True:
    num = int(input('Digite um número: [999 para parar] '))
    if num == 999:
        break
    count += 1
    soma += num
print(f'Você digitou {count} a soma deles é {soma}')