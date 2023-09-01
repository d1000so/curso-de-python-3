frase = input('Digite uma frase: ')
frase = frase.replace(' ', '').upper()
inverso = ''
for i in range(len(frase) -1, -1, -1):
    inverso += frase[i]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('A frase é igual ao inverso!')
else:
    print('A frase não é igual ao inverso!')