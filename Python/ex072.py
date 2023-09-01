# testa se o valor digitado é um número
def isNumber(n):
  try:
    int(n)
  except ValueError:
        return False
  return True

    
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
n = -1
# loop reinicia se não for número ou fora do intervalo solicitado
while not 0 <= n <= 20:
    n = input('Digite um número entre 0 e 20: ')
    if isNumber(n) == False: 
        print('\nTente Novamente: ', end='')
        n = -1
    else:
        n = int(n)
        if not 0 <= n <= 20:
            print('\nTente Novamente: ', end='')
        else:
            print()
            print(f'Você Digitou o número {numeros[n]}.\n')            
            while True: # Quando valor digitado entra no intervalo solicitado
                continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
                if continuar in 'S':  #força o primeiro loop com n=-1
                    n = -1
                    break
                elif continuar in 'N': #sai dos dois loops
                    n = 0
                    break
                else:
                    n = -1
print('Até logo...')
