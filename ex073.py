# print('=' * 6, 'DESAFIO 73/AULA16', '=' * 6)
# print('-=-' * 20)
print('-=-' * 20)
ranking_CB2021 = ('Atlétigo-MG', 'Famengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
                  'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Atlético-PR',
                  'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print(ranking_CB2021)
print('-=-' * 20)
for t in ranking_CB2021:
    print(t)
print('-=-' * 20)
print('Os primeiros 5 são: ')
for c in range(0, 5):
    print(f'{c + 1}º colocado: {ranking_CB2021[c]}')
print('-=-' * 20)
print('Os últimos 4 são: ')
for c in range(3, -1, -1):
    print(f'{len(ranking_CB2021) - c}º colocado: {ranking_CB2021[len(ranking_CB2021) - (c + 1)]}')
print('-=-' * 20)
re_ranking_CB2021 = sorted(ranking_CB2021)
print(f'A lista de times em ordem alfabética: {re_ranking_CB2021}.')
print('-=-' * 20)
pos = ranking_CB2021.index('Chapecoense')
print(f'A Chapecoense está na {pos + 1}ª posição.')
print('-=-' * 20)
print(f'Os 5 primeiros colocados são: {ranking_CB2021[0: 5]}')
print(f'Os 4 últimos colocados são: {ranking_CB2021[-4:]}')
