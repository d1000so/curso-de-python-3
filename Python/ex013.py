salario = float(input('Digite o salario: R$ '))
NovoSal = salario + (salario * 5 / 100)
print('Seu salário era de R$ {:.2f} o novo salário é R$ {:.2f}'.format(salario, NovoSal))