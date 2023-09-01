speed = int(input('Qual a velocidade atual do carro? '))
if speed > 80:
    print(f'\033[1;31;49mMULTADO! Você excedeu o limite permitido que é 80km/h')
    print(f'Você deverá pagar uma multa de R${(speed - 80) * 7:.2f}')
print(f'\033[1;33;49mTenha um bom dia! Dirija com segurança!')