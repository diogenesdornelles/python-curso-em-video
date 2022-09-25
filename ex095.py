# print('=' * 6, 'DESAFIO 93/AULA19', '=' * 6)
# print('-=-' * 20)
jogador = []
analise = {}
c = tot = 0
print('—' * 40)
while True:
    jogador.append(str(input('Nome do jogador: ')))
    jogador.append(int(input(f'Quantas partidas {jogador[0]} jogou: ')))
    jogador.append([])
    for i in range(jogador[1]):
        jogador[2].append(int(input(f'Quantos gols {jogador[0]} marcou na {i + 1} partida: ')))
    for k in range(len(jogador[2])):
        tot += jogador[2][k]
    jogador.append(tot)
    analise[f'jogador{c}'] = jogador[:]
    jogador.clear()
    tot = 0
    c += 1
    r = str(input('Deseja continuar[S/N]: ')).upper().strip()[0]
    while r not in 'SsNn':
        r = str(input('ERRO! Deseja continuar[S/N]: ')).upper().strip()[0]
    if r in 'Nn':
        print('-=-' * 30)
        break
    print('—' * 40)
print('Cod. Nome        Gols                 Total')
print('—' * 40)
f = 0
for v in analise.values():
    print(f'{f:<5}', end='')
    for d in range(len(v)):
        if d == 0:
            print(f'{v[d]:<12}', end='')
        if d == 2:
            print(f'{v[d]}', end=f'')
        if d == 3:
            o = 22 - (3 * len(v[d - 1]))
            print(f'{v[d]:>{o}}', end='')
    print()
    f += 1
print('—' * 40)
while True:
    n = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if n == 999:
        print('FINALIZANDO...VOLTE SEMPRE!')
        break
    if 0 <= n <= (len(analise) - 1):
        print('—— LEVANTAMENTO DE DADOS DO JOGADOR ', end='')
        print(analise[f'jogador{n}'][0])
        w = 1
        for g in analise[f'jogador{n}'][2]:
            print(f'No jogo {w} fez {g} gol(s).')
            w += 1
        print('—' * 40)
    else:
        print(f'ERRO! não existe jogador {n}!')
