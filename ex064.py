print('=' * 6, 'DESAFIO 64/AULA14', '=' * 6)
print('-=-' * 20)
n1 = soma = nt = 0
c = 1
stop = 999
while n1 != stop:
    n1 = int(input(f'Digite o {c}º número[999 para parar]: '))
    soma += n1
    nt += 1
    c += 1
print(f'Foram digitados {nt - 1} números e a soma deles é {soma - stop}')
