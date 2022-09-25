# print('=' * 6, 'DESAFIO 107/AULA22', '=' * 6)
# print('-=-' * 20)

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é  {moeda.moeda(moeda.dobro(p))}')
print(f' {moeda.moeda(p)} aumentado de 10%, temos  {moeda.moeda(moeda.aumentar(p))}')
print(f' {moeda.moeda(p)} reduzido de 13%, temos  {moeda.moeda(moeda.diminuir(p))}')
