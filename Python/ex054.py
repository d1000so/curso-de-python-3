from datetime import date

maiores = 0
menores = 0
ano = 0
atual = date.today().year
for i in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu: '.format(i)))
    if atual - ano >= 21:
        maiores += 1
    else:
        menores += 1
print(maiores, menores)
    