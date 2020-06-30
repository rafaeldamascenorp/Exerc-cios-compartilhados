'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = ((co ** 2) + (ca ** 2)) ** (1/2)
print('A hipotenusa desse triângulo mede {:.2f}.'.format(hip))'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa desse triângulo mede {:.2f}.'.format(hip))


