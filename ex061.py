print('=' * 6, 'DESAFIO 61/AULA14', '=' * 6)
print('-=' * 17)
painel = '10 TERMOS DE UMA PA'
print('{:^35}'.format(painel))
print('-=' * 17)
n1 = int(input('Informe o valor do primeiro termo: '))
r = int(input('Informe a razão da progressão: '))
c = 0
while c < 10:
    nt = n1 + r * c
    print(f' → {nt}', end='')
    c += 1
print(' → ACABOU')
