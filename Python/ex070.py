total = count = caros = baratos = menor = 0
nome = ''
while True:
    produto = str(input('Digite o produto: ')).strip().upper()
    preço = float(input('Preço: R$'))
    total += preço
    count += 1
    if preço > 1000:
        caros += 1
    if count == 1 or preço < menor:
        menor = preço
        nome = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer Continar? ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^45}'.format('Fim do Programa'))
print(f'O total gasto na compra foi R${total:.2f}')
print(f'Cadastrados {caros} produtos que custam mais de R$1000.')
print(f'O produto mais barato foi {nome} e custa R${menor:.2f}.')
