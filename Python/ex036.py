valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do funcionario? R$'))
tempo_anos = int(input('Em quanto tempo pretende financiar? '))
tempo_meses = tempo_anos * 12
margem_salario = salario * 0.3
prestacao = valor_casa / tempo_meses
print(
    f'Para pagar uma casa de R${valor_casa} em um peŕiodo de {tempo_anos} anos aprestação será de R${prestacao}.'
)
if prestacao < margem_salario:
    print('Empréstimo Negado! Margem salarial baixa...')
else:
    print('Empréstimo pode ser CONCEDIDO!...')
