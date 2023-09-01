# ex010-B

import requests
from os import system
system('clear')

cor = {'normal': '\033[0m', 'red': '\033[1;31;49m', 'green': '\033[1;32;49m', 'yellow': '\033[1;33;49m', 'blue': '\033[1;34;49m', 'magenta': '\033[1;35;49m', 'cyan': '\033[1;36;49m'}

key = 'e448e1728c566601123e1a0da380b8b2'
city = 'campinas'
link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
requisicao = requests.get(link)
resposta = requisicao.json()
tatual = float(resposta['main']['temp']) - 273.15
tmin = float(resposta['main']['temp_min']) - 273.15
tmax= float(resposta['main']['temp_max']) - 273.15
flike= float(resposta['main']['feels_like']) - 273.15
print(f'{cor["normal"]}Agora em {city.upper()} \033[4;38;49m{tatual:.1f} °C\033[0m')
print(f'{cor["cyan"]}Mínima: {tmin:.1f} °C')
print(f'{cor["red"]}Máxima: {tmax:.1f} °C')
print(f'{cor["yellow"]}Sensação Térmica: {flike:.1f} °C')
