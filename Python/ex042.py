titulo = 'Analizador de Triâgulos'
print('-=-' * 15)
print(f'{titulo:^45}')
print('-=-' * 15)

a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))

if a + b > c and b + c > a and a + c > b:
    print(f'Os segmentos acima PODEM FORMAR triângulo', end=' ')
    if a != b  and b != c and a != c:
        print('ESCALENO.')
    elif a == b  and b == c:
        print('EQUILÁTERO.')
    else:
        print('ISÓSCELES.')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR um triângulo.')

        
