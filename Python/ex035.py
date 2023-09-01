def triangulo(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return sim
    else:
        return nao

sim = 'PODEM FORMAR'
nao = 'NÃO PODEM FORMAR'
titulo = 'Analizador de Triâgulos'
print('-=-' * 15)
print(f'{titulo:^45}')
print('-=-' * 15)
a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))
print(f'Os segmentos acima {triangulo(a, b, c)} triângulo')
