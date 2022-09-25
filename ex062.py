print('==' * 6, 'DESAFIO 62/AULA14', '==' * 6)
print('==' * 21)
painel = 'GERADOR DE TERMOS DE UMA PA'
print('{:^35}'.format(painel))
print('==' * 21)
n1 = int(input('Informe o valor do primeiro termo: '))
r = int(input('Informe a razão da progressão: '))
q = int(input('Deseja informar quantos termos?'))
qnt = q
while q != 0:
    for c in range(0, q):
        nt = n1 + r * c
        print(f' → {nt}', end='')
    print(' → PAUSA')
    q = int(input('\nDeseja informar mais termos?'))
    nt = int(n1 + r * (c + 1))
    n1 = nt
    qnt += q
print(f'Progressão finalizada com {qnt} termos mostrados.')
