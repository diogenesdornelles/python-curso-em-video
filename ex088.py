# print('=' * 6, 'DESAFIO 88/AULA18', '=' * 6)
# print('-=-' * 20)
from random import randint
from time import sleep
text1 = 'JOGO DA MEGA SENA'
text2 = '< BOA SORTE! >'
print('—' * 30)
print(f'{text1:^30}')
print('—' * 30)
matriz = []
p = int(input('Digite o número de apostas que deseja gerar: '))
print(f'-=-=-=-=-=-= SORTEANDO {p} JOGOS -=-=-=-=-=-=-=')
for c in range(p):
    matriz.append([])
    for j in range(6):
        matriz[c].append(randint(1, 60))
        if j > 0:
            for k in range(0, j - 1):
                if matriz[c][j] == matriz[c][k]:
                    del matriz[c][j]
                    matriz[c].append(randint(1, 60))
for c in range(p):
    matriz[c].sort()
for i in range(p):
    sleep(0.75)
    print(f'Jogo {i + 1:3}:', end=' ')
    for j in range(6):
        print(f'{matriz[i][j]:5}', end=' ')
    print()
print('-=' * 7, '< BOA SORTE!! >', '-=' * 7)

