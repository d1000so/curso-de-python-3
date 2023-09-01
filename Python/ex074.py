from random import randint as rdm

numbers = (rdm(0,10), rdm(0,10), rdm(0,10), rdm(0,10), rdm(0,10),)
print(f'Os números sorteados foram: {numbers}')
print(f'O maior número sorteado foi: {max(numbers)}')
print(f'O menor número sorteado foi: {min(numbers)}')