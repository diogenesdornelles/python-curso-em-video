# print('=' * 6, 'DESAFIO 68/AULA15', '=' * 6)
# print('-=-' * 20)
from time import sleep
from random import randint
print('---' * 20)
text = 'PAR OU ÍMPAR'
print(f'{text:^60}')
print('---' * 20)
c = 0
computer_a = human_b = 0
while True:
    if c % 2 == 0:
        print(f'{c + 1}ª RODADA:')
        print('1º - Computador: ', end='')
        list_a = ['par', 'ímpar']
        computer_a = list_a[randint(0, 1)]
        sleep(2)
        print(f'{computer_a}!')
        if computer_a == 'par':
            human_a = 'ímpar'
        else:
            human_a = 'par'
        sleep(1)
        print(f'2º - Jogador: {human_a}!')
        sleep(1)
        print(f'Digam valores [1 ou 2]:')
        computer_b = randint(1, 2)
        human_b = int(input('Jogador: '))
        while human_b < 1 or human_b > 2:
            print('Valor inválido! informe 1 ou 2')
            human_b = int(input('Jogador: '))
        sleep(1)
        print(f'Computador: {computer_b}')
        sum_a = computer_b + human_b
        if sum_a % 2 == 0:
            result = 'par'
        else:
            result = 'ímpar'
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
        if computer_a == result:
            print(f'O computador VENCEU!')
            print(f'O vencedor escolheu {computer_a} e foram jogados {computer_b} e {human_b} (= {computer_b + human_b})!')
            break
        elif human_a == result:
            print(f'O jogador VENCEU!')
            print(f'O vencedor escolheu {human_a} e foram jogados {computer_b} e {human_b} (= {computer_b + human_b})!')
            print('Vamos jogar de novo...')
            c += 1
            print('---' * 20)
    else:
        print(f'{c + 1}ª RODADA:')
        option = int(input('1º Jogador [0 para par ou 1 para ímpar]: '))
        while option < 0 or option > 1:
            print('Valor inválido! informe 0 ou 1')
            option = int(input('informe 0 para par ou 1 para ímpar: '))
        list_a = ['par', 'ímpar']
        human_a = list_a[option]
        if human_a == 'par':
            computer_a = 'ímpar'
        elif human_a == 'ímpar':
            computer_a = 'par'
        print(f'Jogador: {human_a}!')
        print(f'Computador: {computer_a}!')
        sleep(1)
        print(f'Digam valores [1 ou 2]:')
        computer_b = randint(1, 2)
        human_b = int(input('Jogador: '))
        while human_b < 1 or human_b > 2:
            print('Valor inválido! informe 1 ou 2')
            human_b = int(input('Jogador: '))
        sleep(1)
        print(f'Computador: {computer_b}')
        sum_a = computer_b + human_b
        if sum_a % 2 == 0:
            result = 'par'
        else:
            result = 'ímpar'
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
        if computer_a == result:
            print(f'O computador VENCEU!')
            print(f'O vencedor escolheu {computer_a} e foram jogados {computer_b} e {human_b} (= {computer_b + human_b})!')
            break
        elif human_a == result:
            print(f'O jogador VENCEU!')
            print(f'O vencedor escolheu {human_a} e foram jogados {computer_b} e {human_b} (= {computer_b + human_b})!')
            print('Vamos jogar de novo...')
            c += 1
            print('---' * 20)
print('')
if c == 1:
    print(f'GAME OVER! O jogador ganhou {c} vez apenas.')
elif c > 1:
    print(f'GAME OVER! O jogador ganhou {c} vezes consecutivas.')
