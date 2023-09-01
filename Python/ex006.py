#ex006

cor = {'normal': '\033[0m', 'red': '\033[1;31;49m', 'green': '\033[1;32;49m', 'yellow': '\033[1;33;49m', 'blue': '\033[1;34;49m', 'magenta': '\033[1;35;49m', 'cyan': '\033[1;36;49m'}

print(f'{cor["cyan"]}Digite um número:', end=' ')
num = int(input())
print(f'{cor["red"]}O dobro de {num} é: {num * 2}{cor["green"]}')
print(f'{cor["blue"]}O triplo de {num} é: {num * 3}{cor["green"]}')
print(f'{cor["magenta"]}A raiz de {num} é: {num ** (1/2):.0f}{cor["green"]}')
