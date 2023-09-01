palavra = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trablhar', 'mercado', 'programar', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
for i, p in enumerate(palavra):
    print(f'\nNa palavra {palavra[i].upper()} temos ', end='')
    for v in p:
        if v in vogais:
            print(v, end=' ')
