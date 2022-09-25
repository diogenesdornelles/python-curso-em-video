# print('=' * 6, 'DESAFIO 109/AULA22', '=' * 6)
# print('-=-' * 20)

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.moeda(p)} é  {moeda.dobro(p, True)}')
print(f'{moeda.moeda(p)} aumentado de 10%, temos  {moeda.aumentar(p, True)}')
print(f'{moeda.moeda(p)} reduzido de 13%, temos  {moeda.diminuir(p, True)}')
