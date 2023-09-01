# ex009

import os
fator = int(input('Qual tabuada quer estudar? '))
tamanho = len('*   TABUADA  DO{:^9}*'.format(fator))
os.system('clear')
print('\n', '*' * tamanho)
print(' *   TABUADA  DO{:^9}*'.format(fator))
print('', '*' * tamanho)
for i in range(1, 11,1):
  print(' *{:^7}X{:^7}={:^7}*'.format(fator, i, fator * i, ))
print('', '*' * tamanho)