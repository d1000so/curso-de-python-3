#ex003

cor = {'normal': '\033[0m', 'red': '\033[1;31;49m', 'green': '\033[1;32;49m', 'yellow': '\033[1;33;49m', 'blue': '\033[1;34;49m', 'magenta': '\033[1;35;49m', 'cyan': '\033[1;36;49m'}

print(f'{cor["yellow"]}Digite o primeiro número: ', end='')
n1 = int(input())
print(f'{cor["cyan"]}Digite o segundo número: ', end='')
n2 = int(input())
soma = n1 + n2
print(f'{cor["red"]}A soma entre {n1} e {n2} é {soma}.')
