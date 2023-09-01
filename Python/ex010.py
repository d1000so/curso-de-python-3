import requests
from datetime import datetime
from os import system

cor = {'normal': '\033[0m', 'red': '\033[1;31;49m', 'green': '\033[1;32;49m', 'yellow': '\033[1;33;49m', 'blue': '\033[1;34;49m', 'magenta': '\033[1;35;49m', 'cyan': '\033[1;36;49m'}
system('clear')
r = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
arquivo = r.json()
time_stamp = int(arquivo['USDBRL']['timestamp'])
valor = float(arquivo['USDBRL']['high'])
date = datetime.fromtimestamp(time_stamp)
str_date_time = date.strftime('%d-%m-%Y às %H:%M:%S')
print(f'{cor["cyan"]}Cotação em {cor["red"]}{str_date_time}')
print(f'{cor["cyan"]}USDT-BRL: {cor["green"]}R$ {valor:.2f}')
