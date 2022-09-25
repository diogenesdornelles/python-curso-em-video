# print('=' * 6, 'DESAFIO 79/AULA17', '=' * 6)
# print('-=-' * 20)
list_1 = []
while True:
    c = 0
    while c == 0:
        n = int(input(f'Digite um valor: '))
        if n not in list_1:
            list_1.append(n)
            print('Valor adicionado com sucesso...')
            c = 1
        elif n in list_1:
            print(f'ERRO! Número já consta da lista. ', end='')
            c = 0
    r = str(input('Deseja continuar[S/N]: ').strip().lower()[0])
    while r != 's' and r != 'n':
        r = str(input('ERRO! Deseja continuar[S/N]: ').strip().lower()[0])
    if r == 'n':
        break
list_1.sort()
print(f'Você digitou os valores {list_1}')
