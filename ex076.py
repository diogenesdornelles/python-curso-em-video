# print('=' * 6, 'DESAFIO 76/AULA16', '=' * 6)
# print('-=-' * 20)
tuple_1 = ('Pão', 1.00,
           'Leite', 1.50,
           'Café', 6.50,
           'Empada', 3.25,
           'Nata', 4.00,
           'Iogurte', 3.00,
           'Cuca', 6.00,
           'Manteiga', 7.00,
           'Refrigerante', 7.00,
           'Pizza', 10.00,
           'Sanduíche', 9.00,
           'Bolo de morango', 100.00)
text1 = 'LISTAGEM DE PREÇOS'
print('—' * 40)
print(f'{text1:^39}')
print('—' * 40)
text2 = 'R$'
c1 = c2 = 0
for c in range(0, len(tuple_1), 2):
    c1 = tuple_1[c]
    c2 = tuple_1[c + 1]
    print(f'{c1:.<15}{text2:.>18}{c2:>7.2f}')
print('—' * 40)
