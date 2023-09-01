#ex002

cor = {'normal': '\033[0m', 'red': '\033[1;31;49m', 'green': '\033[1;32;49m', 'yellow': '\033[1;33;49m', 'blue': '\033[1;34;49m', 'magenta': '\033[1;35;49m', 'cyan': '\033[1;36;49m'}

print(f'{cor["yellow"]}Digite seu nome:', end=' ')
nome = str(input())
print(f'{cor["cyan"]}Muito prazer em conhecer {nome.capitalize()}!')
