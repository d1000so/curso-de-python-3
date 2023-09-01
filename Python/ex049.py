# ex009

import os
fator = int(input('Qual tabuada quer estudar? '))
tamanho = len('*   TABUADA  DO{:^9}*'.format(fator))
os.system('clear')
print('\n', '*' * tamanho)
print(f' *   TABUADA  DO{:^9}*'.format(fator))
print('', '*' * tamanho)
for i in range(1, 11,1):
  print(f' *{fator:^7}X{i:^7}={fator * i:^7}*')
print('', '*' * tamanho)