from random import choice
from time import sleep
print('='*6, 'DESAFIO 45/AULA12', '='*6)
print('-=-'*20)
print('                        JOKENPO                              ')
print('-=-'*20)
print('Suas opções: pedra, tesoura ou papel:')
human = str(input())
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('+-'*20)
sleep(1)
PC = choice(['pedra', 'tesoura', 'papel'])
if PC == human:
    print('Jogo EMPATADO')
elif PC == 'pedra' and human == 'tesoura':
    print('O computador VENCEU!')
elif PC == 'pedra' and human == 'papel':
    print('O humano VENCEU!')
elif PC == 'papel' and human == 'pedra':
    print('O computador VENCEU!')
elif PC == 'papel' and human == 'tesoura':
    print('O humano VENCEU!')
elif PC == 'tesoura' and human == 'papel':
    print('O computador VENCEU!')
elif PC == 'tesoura' and human == 'pedra':
    print('O humano VENCEU!')
else:
    print('Jogada INVÁLIDA!')
print('+-'*20)
print('Computador jogou {}! \nhumano jogou {}!'.format(PC.upper(), human.upper()))
print('+-'*20)
