
print('='*6, 'DESAFIO 51/AULA13', '='*6)
print('=='*20)
painel = '10 TERMOS DE UMA PA'
print('{:^35}'.format(painel))
print('=='*20)
n1 = int(input('Informe o valor do primeiro termo: '))
r = int(input('Informe a razão da progressão: '))
for c in range(0, 10):
    nt = n1 + r * c
    print((f' → {nt}'), end='')
print(' → ACABOU')
    