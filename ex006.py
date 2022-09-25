# ler um número inteiro e mostra dobro, triplo e raizq
print('='*6,'DESAFIO 06/AULA07','='*6)
n1 = int(input('Digite um número: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
print('O dobro de {} é {}, o triplo é {} e a sua raiz quadrada é {}'.format(n1, d, t, r))