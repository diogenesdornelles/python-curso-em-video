# print('=' * 6, 'DESAFIO 99/AULA20', '=' * 6)
# print('-=-' * 20)
from time import sleep


#  inicio da função:
def maior(* num):
    n = len(num)
    print('-=-' * 30)
    print('Analisando os valores passados ...')
    maj = 0
    for c in num:
        print(f'{c}', end=' ')
        if c > maj:
            maj = c
    print(f'Foram informados {n} valores ao todo.')
    print(f'O maior valor informado foi {maj}.')


#  inicio do programa principal:

sleep(1)
maior(4, 3, 2, 7, 8)
sleep(1)
maior(1, 3)
sleep(1)
maior(6, 4, 7)
sleep(1)
maior(0, 1, 0, 3)
sleep(1)
maior(6)
sleep(1)
maior(9, 7, 1, 5, 3, 9, 6, 4, 5, 2, 7)
