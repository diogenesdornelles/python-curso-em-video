# print('=' * 6, 'DESAFIO 107/AULA22', '=' * 6)
# print('-=-' * 20)
import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p:.2f} é {moeda.metade(p):.2f}')
print(f'O dobro de {p:.2f} é  {moeda.dobro(p):.2f}')
print(f' {p:.2f} aumentado de 10%, temos  {moeda.aumentar(p):.2f}')
print(f' {p:.2f} reduzido de 13%, temos  {moeda.diminuir(p):.2f}')
