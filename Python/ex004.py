#ex004

cor = {'normal': '\033[0m', 'red': '\033[1;31;49m', 'green': '\033[1;32;49m', 'yellow': '\033[1;33;49m', 'blue': '\033[1;34;49m', 'magenta': '\033[1;35;49m', 'cyan': '\033[1;36;49m'}

print(f'{cor["yellow"]}Digite algo:', end=' ')
stuff = input()
print(f'{cor["red"]}É número?  {cor["cyan"]}{stuff.isnumeric()}')
print(f'{cor["green"]}É alfabético?  {cor["cyan"]}{stuff.isalpha()}')
print(f'{cor["blue"]}É minúsculo?  {cor["cyan"]}{stuff.islower()}')
print(f'{cor["magenta"]}É captalizado?  {cor["cyan"]}{stuff.istitle()}')
print(f'{cor["normal"]}É espaco?  {cor["cyan"]}{stuff.isspace()}')
