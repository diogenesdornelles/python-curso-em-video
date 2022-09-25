#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
print('='*6, 'DESAFIO 28/AULA10', '='*6)
from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
numb1 = randint(0, 5)
numb2 = int(input('Em que número pensei?'))
print('PROCESSANDO...')
sleep(3)
if numb1 == numb2:
    print('PARABÉNS! Você conseguiu vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(numb1, numb2))
print('--FIM--')


