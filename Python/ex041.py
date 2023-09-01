from datetime import date

ano_nasc = int(input('Digite o ano de nascimento: ').strip())
idade = date.today().year - ano_nasc

categoria = ['MIRIM', 'INFANTIL', 'JÚNIOR', 'SÊNIOR', 'MASTER']

print(f'O atleta tem {idade} anos.')
if idade < 10:
    print(f'Classificação: {categoria[0]}')
elif idade < 15:
    print(f'Classificação: {categoria[1]}')
elif idade < 20:
    print(f'Classificação: {categoria[2]}')
elif idade < 25:
    print(f'Classificação: {categoria[3]}')
elif idade >= 25:
    print(f'Classificação: {categoria[4]}')
