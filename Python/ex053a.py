teste = ('APOS A SOPA', 'A SACADA DA CASA', 'A TORRE DA DERROTA', 'O LOBO AMA O BOLO', 'ANOTARAM A DATA DA MARATONA')
frase = input('Digite uma frase: ')
frase = frase.replace(' ', '')
pal = frase[::-1]
print(f'O inverso de {frase} é {frase[::-1]}')
if frase == pal:
    print('A frase é igual ao inverso!')
else:
    print('A frase não é igual ao inverso!')