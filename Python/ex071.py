print('=' * 43)
print('{:^43}'.format('BANCO ED'))
print('=' * 43)
total = int(input('\nQue valor você quer sacar? '))
print('\nTOTAL:\n')
totcéd = 0
céd = 50
while True:
    if total >= céd:
        total -= céd 
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'{totcéd:>10} cédulas de R${céd:>3}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('\n'+'=' * 43)
print('Volte sempre ao BANCO ED! Tenha um bom dia!')