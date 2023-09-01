import math
cOp = float(input('Digite o cateto oposto: '))
cAd = float(input('Digite o cateto adjacente: '))
print('A hipotenusa do triangulo é {:.2f}'.format(math.hypot(cOp, cAd)))
