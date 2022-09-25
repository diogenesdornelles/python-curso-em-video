# print('=' * 6, 'DESAFIO 85/AULA18', '=' * 6)
# print('-=-' * 20)
list_1 = [[], []]
for c in range(7):
    n = int(input(f'Digite o {c + 1}º valor: '))
    if n % 2 == 0:
        list_1[0].append(n)
    elif n % 2 != 0:
        list_1[1].append(n)
list_1[0].sort()
list_1[1].sort()
print('-=-' * 20)
print(f'Os valores pares digitados foram {list_1[0]}')
print(f'Os valores pares digitados foram {list_1[1]}')


