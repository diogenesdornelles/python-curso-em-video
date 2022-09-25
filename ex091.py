# print('=' * 6, 'DESAFIO 91/AULA19', '=' * 6)
# print('-=-' * 20)
from random import randint
from time import sleep
partida = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)
           }
a = str(input())
print('== Valores sorteados ==')
for k, v in partida.items():
    sleep(0.75)
    print(f'   O {k} tirou {v} no dado')
print('== RANKING DOS JOGADORES == ')
partida1 = {}
for c in range(6, 0, -1):
    for k, v in partida.items():
        if v == c:
            partida1[k] = c
c = 1
for k, v in partida1.items():
    sleep(0.75)
    print(f'   {c}º lugar: {k} com {v} pontos.')
    c += 1

#  Métodos:
#  partida = dict(sorted(partida.items(), key=lambda item: item[1]))
#  print(partida)
#  import operator
#  partida = sorted(partida.items(), key=operator.itemgetter(1))
#  print(partida)







