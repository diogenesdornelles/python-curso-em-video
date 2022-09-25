# print('=' * 6, 'DESAFIO 84/AULA18', '=' * 6)
# print('-=-' * 20)
list_1 = []
dados = []
pesado = []
leve = []
tot = mai = mi = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    list_1.append(dados[:])
    dados.clear()
    r = str(input('Deseja cadastrar outra pessoa [S/N]: ')).upper().strip()[0]
    if r not in 'SsNn':
        r = str(input('ERRO! Deseja cadastrar outra pessoa [S/N]: ')).upper().strip()[0]
    if r == 'N' or r == 'n':
        break
    tot += 1
for p in range(len(list_1)):
    if list_1[p][1] > mai:
        mai = list_1[p][1]
    if p == 0:
        mi = list_1[p][1]
    elif p != 0:
        if list_1[p][1] < mi:
            mi = list_1[p][1]
for j in list_1:
    if mai == j[1]:
        pesado.append(j[0])
    elif mi == j[1]:
        leve.append(j[0])
print(f'Ao todo, você cadastrou {tot + 1} pessoas.')
print(f'O maior peso foi de {mai}KG. Peso de {pesado}.')
print(f'O menor peso foi de {mi}KG. Peso de {leve}.')
