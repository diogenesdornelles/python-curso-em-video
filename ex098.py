# print('=' * 6, 'DESAFIO 98/AULA20', '=' * 6)
# print('-=-' * 20)
from time import sleep


# início da função:
def contador(i, f, p):
    if i == f:
        sleep(0.5)
        print(f'{i}.')
    if i < f:
        sleep(0.5)
        print(f'{i}..', end='')
        while i < f:
            i += p
            sleep(0.5)
            print(f'{i}..', end='')
    elif i > f:
        sleep(0.5)
        print(f'{i}..', end='')
        while i > f:
            i -= p
            sleep(0.5)
            print(f'{i}..', end='')
    print('FIM!')


#  início do programa principal:
print('-=-' * 20)
print('Contagem de 1 até 10 de 1 em 1:')
contador(1, 10, 1)
print('-=-' * 20)
print('Contagem de 10 até 1 de 1 em 1:')
contador(10, 1, 1)
print('-=-' * 20)
print('Contagem personalizada: ')
contador(i=int(input('Informe o início da contagem: ')), f=int(input('Informe o fim da contagem: ')),
         p=abs(int(input('Informe o passo: '))))
