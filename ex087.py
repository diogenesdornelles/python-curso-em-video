# print('=' * 6, 'DESAFIO 87/AULA18', '=' * 6)
# print('-=-' * 20)
matriz = []
s = s1 = m = 0
for i in range(3):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
print('-=-' * 20)
for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            s += matriz[i][j]
        if j == 2:
            s1 += matriz[i][j]
        if i == 1:
            if matriz[i][j] > m:
                m = matriz[i][j]
        print(f'[  {matriz[i][j]}  ]', end=' ')
    print()
print(f'A soma dos valores pares é {s}')
print(f'A soma dos valores da terceira coluna é {s1}')
print(f'O maior valor da segunda linha é {m}')
