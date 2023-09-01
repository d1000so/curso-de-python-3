num = int(input('Digite um número inteiro: ').strip())
print('Para qual das bases deseja converter?')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')


bases = ['DECIMAL', 'BINÁRIO', 'OCTAL', 'HEXADECIMAL']

while True:
    choice = int(input('Sua opção: ').strip())

    if choice == 1:
        print(f'{num} convertido para {bases[1]} é igual a {bin(num)[2:]}')
        break
    elif choice == 2:
        print(f'{num} convertido para {bases[2]} é igual a {oct(num)[2:]}')
        break
    elif choice == 3:
        print(f'{num} convertido para {bases[3]} é igual a {hex(num)[2:]}')
        break
    else:
        print('Opção não é válida')
        pass

