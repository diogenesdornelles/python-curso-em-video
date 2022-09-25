from random import randint
from time import sleep
from operator import itemgetter
partida = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)
           }
ranking = {}
print('== Valores sorteados ==')
for k, v in partida.items():
    sleep(0.75)
    print(f'   O {k} tirou {v} no dado')
ranking = sorted(partida.items(), key=itemgetter(1), reverse=True)  # retorna resultado em forma de lista, com tuplas
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(0.75)