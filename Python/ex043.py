peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'Seu IMC é de: {imc:.1f}')
if imc < 18.5:
    print(f'Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print(f'Parabens! você está na faixa de PESO IDEAL')
elif 25 <= imc < 30:
    print(f'Você está em SOBREPESO')
elif 30 <= imc < 40:
    print(f'Você está em OBESIDADE, Cuidado!')
else:
    print(f'Você está em OBESIDADE MORBIDA, procure um médico!')
