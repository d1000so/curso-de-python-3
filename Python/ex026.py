nome = input('Digite seu nome completo: ')
lista_nome_completo = nome.split()
count_nomes = len(lista_nome_completo)
last_nome = lista_nome_completo[count_nomes - 1]
print(lista_nome_completo[0].title(), last_nome.title())


