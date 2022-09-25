print('=' * 6, 'DESAFIO 60/AULA14', '=' * 6)
print('-=-' * 20)
numb1 = int(input('Digite um número para calcular o fatorial: '))
print(f'Calculando {numb1}! = ', end='')
fact = 1
while numb1 >= 2:
    fact = fact * numb1
    print(f' {numb1} X', end='')
    numb1 -= 1
print(f' {numb1} = {fact}.')

