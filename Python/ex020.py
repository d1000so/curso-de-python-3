import random
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])