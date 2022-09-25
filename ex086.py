# print('=' * 6, 'DESAFIO 86/AULA17', '=' * 6)
# print('-=-' * 20)
matriz = []
for i in range(3):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
print('-=-' * 20)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()
