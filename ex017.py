#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.
from math import sqrt, hypot
print('='*6, 'DESAFIO 17/AULA08', '='*6)
cat1 = float(input('Informe o comprimento do cateto oposto: '))
cat2 = float(input('Informe o comprimento do cateto adjacente: '))
#hip = sqrt(pow(cat1,2) + pow(cat2,2))
hip = hypot(cat1, cat2)
print('Se um triângulo retângulo tiver o cateto oposto igual a {} '.format(cat1), end='')
print('e o cateto adjacente igual a {} '.format(cat2), end='')
print(', então a hipotenusa será igual a {}.'.format(hip))