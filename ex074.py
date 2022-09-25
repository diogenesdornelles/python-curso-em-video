# print('=' * 6, 'DESAFIO 74/AULA16', '=' * 6)
# print('-=-' * 20)
from random import randint
tuple_ex = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(tuple_ex)
print(f'Os valores sorteados foram: ', end=' ')
for c in range(0, 5):
    print(f'{tuple_ex[c]}', end=' ')
min = min(tuple_ex)
print(f'\nO menor número é: {min}.')
max = max(tuple_ex)
print(f'O maior número é: {max}.')
