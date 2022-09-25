# print('=' * 6, 'DESAFIO 75/AULA16', '=' * 6)
# print('-=-' * 20)
tuple_a = (int(input(f'Digite um número: ')),
           int(input(f'Digite outro número: ')),
           int(input(f'Digite mais um número: ')),
           int(input(f'Digite o último número: ')))
print(f'Você digitou os valores {tuple_a}.')
print(f'O Valor 9 apareceu {tuple_a.count(9)} vez(es)')
if 3 in tuple_a:
    c3 = tuple_a.index(3)
    print(f'O valor 3 apareceu na {c3 + 1}ª posição')
else:
    print(f'O valor 3 não foi digitado')
s = 0
print('Os valores pares digitados foram', end=' ')
for cont in range(0, 4):
    c2 = tuple_a[cont]
    if c2 % 2 == 0:
        s += 1
        print(f'{c2}', end=' ')

