from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Digite o ano de nascimento: ').strip())
idade = ano_atual - ano_nasc
faltam = 18 - idade
foi = idade - 18

print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.')

if idade < 18:
    print(f'Ainda faltam {faltam} anos para você se alistar.')
    print(f'Seu alistamento será no ano de {ano_atual + faltam}.')
elif idade > 18:
    print(f'Você já deveria ter se alistado {foi} anos atrás.')
    print(f'Seu alistamento foi em {ano_atual - foi}.')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 0:
    print('Voce precisa nascer primeiro, antes de se alistar!!!')



