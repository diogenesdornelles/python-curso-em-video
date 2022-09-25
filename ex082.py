# print('=' * 6, 'DESAFIO 82/AULA17', '=' * 6)
# print('-=-' * 20)
list_1 = []
list_2 = []
list_3 = []
while True:
    list_1.append(int(input('Digite um número: ')))
    r = str(input('Deseja digitar outro número?[S/N]')).strip().upper()[0]
    while r not in 'SsNn':
        r = str(input('ERRO! Deseja digitar outro número?[S/N]')).strip().upper()[0]
    if r == 'N':
        for c in range(0, len(list_1)):
            if list_1[c] % 2 == 0:
                list_2.append(list_1[c])
            else:
                list_3.append(list_1[c])
        break
print('-=-' * 20)
print(f'Os números digitados foram: {list_1}')
print(f'Os números pares digitados foram: {list_2}')
print(f'Os números ímpares digitados foram: {list_3}')
