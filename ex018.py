#
from math import sin, cos, tan, radians
print('='*6, 'DESAFIO 18/AULA08', '='*6)
angle = float(input('Informe o valor do ângulo: '))
anglesin = sin(radians(angle))
anglecos = cos(radians(angle))
angletan = tan(radians(angle))
print('O seno de {} é igual a {:.2f}'.format(angle, anglesin))
print('O cosseno de {} é igual a {:.2f}'.format(angle, anglecos))
print('A tangente de {} é igual a {:.2f}'.format(angle, angletan))

