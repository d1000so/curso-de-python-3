media = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
count_mulher_menor20 = 0
for p in range(1,5):
    print(f'----- {p}ª PESSOA -----')
    nome = input('Nome: ').strip().title()
    idade = int(input('Idade: ').strip())
    sexo = input('Sexo: ').strip().upper()
    media += idade
    if sexo == 'F':
        if idade < 20:
            count_mulher_menor20 += 1
    else:
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome
            
print(f'A média de idade do grupo é de {media / 4:.2f} anos.')
print(f'O homem mais velho tem {idade_homem_mais_velho} anos e se chama {nome_homem_mais_velho}.')
print(f'Ao todo são {count_mulher_menor20} mulheres menores de 20 anos.')