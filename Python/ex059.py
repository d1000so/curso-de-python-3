from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print(f'A soma entre {n1} + {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'A resultado entre {n1} x {n2} = {n1 * n2}')
    elif opcao == 3:
        print(f'Entre {n1} e {n2} o maior é {max(n1, n2)}')
    elif opcao == 4:
        print('Informe os números novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('finalizando...')
    else:
        print('Opção inválida! Tente novamente: ')
    print('=-=' * 10)
    sleep(1.5)
print(' Fim do programa!')
        