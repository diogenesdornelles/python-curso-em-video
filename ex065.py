print('=' * 6, 'DESAFIO 65/AULA14', '=' * 6)
print('-=-' * 20)
n1 = soma = maj = mi = c = 0
stop = 'S'
while stop != 'N':
    n1 = int(input(f'Digite o {c + 1}º número: '))
    soma += n1
    c += 1
    if n1 > maj:
        maj = n1
    if mi == 0:
        mi = n1
    elif n1 < mi:
        mi = n1
    stop = str(input('Deseja continuar[s/n]: ')).upper().strip()[0]
media = float(soma/(c))
print(f'O maior valor digitado foi {maj}.')
print(f'O menor valor digitado foi {mi}.')
print(f'A média dos valores digitados foi {media:.2f}.')

