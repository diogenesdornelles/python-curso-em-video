# print('=' * 6, 'DESAFIO 106/AULA21', '=' * 6)
# print('-=-' * 20)
from time import (sleep)


def painel1():
    sleep(0.75)
    a = 'SISTEMA DE AJUDA PyHELP'
    b = len(a) + 4
    print('\033[1;102m\033[1;97m~' * b)
    print(f'  {a}')
    print('~' * b)


def painel2(x):
    sleep(0.75)
    c = 'Acessando o manual do comando ' + x
    b = len(c) + 4
    print('\033[1;104m\033[1;97m~' * b)
    print(f'  {c}')
    print('~' * b)


while True:
    painel1()
    sleep(0.75)
    f = str(input('\033[0;0mFunção ou biblioteca("fim" para terminar): '))
    if f == 'fim':
        break
    painel2(f)
    sleep(0.75)
    print('\033[1;107m\033[1;30m ')
    help(f)
print('Finalizando...')
