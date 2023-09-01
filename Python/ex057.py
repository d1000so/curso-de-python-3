sexo = 'sexo'
while sexo not in 'FM':
    sexo = input('Informe seu sexo: [ M/F ] ').strip().upper()[0]
    if sexo not in 'FM':
        print('Dados inválidos. Por favor,' , end=' ')
    else:
        print(f'Sexo {sexo} registrado com sucesso!')
    