opcao = 'S'
count = soma = media = maior = menor = num = 0
while opcao in 'S':
    num = int(input('Digite um número: '))
    soma += num
    count += 1
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Quer continuar? [S/N] ')).upper()
media = soma / count
print(f'Você digitou {count} números e a média foi {media:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
    