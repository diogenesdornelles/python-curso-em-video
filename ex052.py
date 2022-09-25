
print('='*6, 'DESAFIO 52/AULA13', '='*6)
print('-=-'*20)
n1 = int(input('Informe um número: '))
s = 0
t = 0
for c in range(1, n1 + 1):
    if n1 % c != 0:
        s += 1
        print('\033[1;31m{} '.format(c), end='')
    elif n1 % c == 0:
        t += 1
        print('\033[1;33m{} '.format(c), end='')
if t > 2:
    print(f'\n\033[1;96mO número {n1} foi divisível {t} vezes!')
    print('E por isso ele NÃO É PRIMO!')
else:
    print(f'\n\033[1;96mO número {n1} foi divisível {t} vezes!')
    print('E por isso ele É PRIMO!')
