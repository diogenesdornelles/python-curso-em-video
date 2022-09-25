print('=' * 6, 'DESAFIO 63/AULA14', '=' * 6)
print('-=-' * 15)
nt = int(input('Digite o número de termos da sequência de Fibonacci: '))
n1 = 0
n2 = 1
cont = 1
print(f'(1º){n1}..(2º){n2}..', end='')
while cont < nt - 1:
    fib = n1 + n2
    n1 = n2
    n2 = fib
    cont += 1
    print(f'({cont + 1}º){fib}..', end='')
