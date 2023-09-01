import os
from time import sleep

os.system('clear')
msg = ' LOJAS DO DIMMY '
print(f'{msg:=^50}')
valor = float(input('Valor das compras: R$ ').strip())
while True:
    print("""FORMA DE PAGAMENTO
    [ 1 ] à vista Dinheiro/ PIX
    [ 2 ] à vista Cartão
    [ 3 ] 2X no Cartão
    [ 4 ] 3X ou mais no Cartão""")
    off10 = valor * 0.9
    off5  = valor * 0.95
    forma = int(input('Qual a opção: ').strip())
    if 5 > forma >= 3:
        while True:
            parcelas = int(input('Quantas parcelas? [ até 10X ] '))
            if parcelas == 2:
                print(f'Sua compra será parcelada em 2X de de R${valor / 2:.2f} SEM JUROS.')
                print(f'Sua compra terá o valor de R${valor:.2f}')
                break
            elif 11 > parcelas >= 3:
                final = (valor * 1.2)
                print(f'Sua compra será parcelada em {parcelas}X de de R${final / parcelas:.2f} COM JUROS.')
                print(f'Sua compra de R${valor:.2f} vai custar R${final:.2f} no final.')
                break
            else:
                print('Opção inválida!')
                sleep(2)
        break
    elif forma == 1:
        print(f'Sua compra de R${valor:.2f} vai ficar em R${off10:.2f} com 10% de deconto.')
        break
    elif forma == 2:
        print(f'Sua compra de R${valor:.2f} vai ficar em R${off5:.2f} com 5% de deconto.')
        break
    else:
        os.system('clear')
        print('Opção inválida!')
        sleep(2)
print('fim')
