salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    salario_novo = salario * 1.15
else:
    salario_novo = salario * 1.1

print(f'Quem ganhava {salario:.2f} passa a ganhar {salario_novo:.2f} agora.')