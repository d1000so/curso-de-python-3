# ex067
count = num = 0
while True:
    num = int(input(' Quer ver qual tabuada? '))
    print('~' * 25)
    if num < 0:
        break
    while True:
        count += 1
        produto = num * count
        print(f'{num:^7}x{count:^7}={produto:^7}')
        if count == 10:
            print('~' * 25)
            count = 0
            break
print('Programa encerrado. Volte sempre...')
     
    
