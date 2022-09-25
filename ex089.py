# print('=' * 6, 'DESAFIO 89/AULA18', '=' * 6)
# print('-=-' * 20)
lista_1 = []
c = 0
while True:
    lista_1.append([])
    lista_1[c].append(str(input(f'Nome do {c + 1}º aluno: ')))
    a = float(input(f'Nota 1: '))
    b = float(input(f'Nota 2: '))
    lista_1[c].append([a, b])
    lista_1[c].append((a + b)/2)
    r = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if r not in 'SsNn':
        r = str(input('ERRO! Deseja continuar [S/N]? '))
    if r == 'N' or r == 'n':
        break
    c += 1
print('-=-' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('—' * 30)
for c in range(len(lista_1)):
    print(f'{c:<4}', end='')
    print(f'{lista_1[c][0]:<10}', end='')
    print(f'{lista_1[c][2]:>8}')
print('—' * 30)
while True:
    n = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    if n == 999:
        print('FINALIZANDO...')
        break
    if n <= (len(lista_1) - 1):
        print(f'As notas de {lista_1[n][0]} são {lista_1[n][1]}')
        print('—' * 30)
    elif n > (len(lista_1) - 1):
        print('ERRO! Aluno não cadastrado!', end='')
print('—' * 30)
