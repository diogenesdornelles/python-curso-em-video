# print('=' * 6, 'DESAFIO 100/AULA20', '=' * 6)
# print('-=-' * 20)
from random import randint
from time import sleep


#  início da função sortear:
def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    num = []
    for c in range(5):
        a = (randint(0, 10))
        sleep(0.5)
        print(a, end=' ')
        num.append(a)
    print('PRONTO!')
    return num


#  início da função somar par:
def somapar(valores):
    s = 0
    for c in valores:
        if c % 2 == 0:
            s += c
    return s


#  início do programa:
lista = sorteia()
soma = somapar(lista)
print(f'Somando os valores de {lista}, temos {soma}.')
