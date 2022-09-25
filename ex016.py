#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
print('='*6, 'DESAFIO 16/AULA08', '='*6)
from math import trunc
num = float(input('Digite um número qualquer contendo vírgula: '))
dec = trunc(num)
print('O número {} tem a parte inteira {}.'.format(num, dec))

