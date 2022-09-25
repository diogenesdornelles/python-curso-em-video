# print('=' * 6, 'DESAFIO 78/AULA17', '=' * 6)
# print('-=-' * 20)
maj = mi = 0
list_1 = []
list_2 = []
list_3 = []
for c in range(0, 5):
    list_1.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-=-' * 20)
print(f'Você digitou os valores {list_1}')
for c in range(0, 5):
    if list_1[c] > maj:
        maj = list_1[c]
    if c == 0:
        mi = list_1[c]
    elif c > 0:
        if mi > list_1[c]:
            mi = list_1[c]
for c in range(0, len(list_1)):
    if list_1[c] == maj:
        list_2.append(c)
    if list_1[c] == mi:
        list_3.append(c)
print(f'O maior valor digitado foi {maj} nas posições ', end='')
for c in range(0, len(list_2)):
    print(f'{list_2[c]}... ', end='')
print(f'\nO menor valor digitado foi {mi} nas posições ', end='')
for c in range(0, len(list_3)):
    print(f'{list_3[c]}... ', end='')
