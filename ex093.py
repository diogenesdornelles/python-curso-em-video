# print('=' * 6, 'DESAFIO 93/AULA19', '=' * 6)
# print('-=-' * 20)
jogador = {'nome': str(input('Nome do jogador: '))}
jogador['partidas'] = int(input(f'Número de partidas que {jogador["nome"]} jogou: '))
for c in range(jogador['partidas']):
    jogador[f'gol(s) partida{c + 1}'] = int(input(f'Número de gol(s) na {c + 1}ª partida: '))
s = 0
c = 1
for k, v in jogador.items():
    if k == f'gol(s) partida{c}':
        s += v
        c += 1
jogador['total de gol(s)'] = s
print('-=-' * 20)
print(jogador)
print('-=-' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-' * 20)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
c = 1
for k, v in jogador.items():
    if k == f'gol(s) partida{c}':
        print(f'    => Na partida {c}, fez {v} gol(s).')
        c += 1
print(f'Foi um total de {jogador["total de gol(s)"]} gol(s).')
