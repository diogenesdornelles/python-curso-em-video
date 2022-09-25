# print('=' * 6, 'DESAFIO 92/AULA19', '=' * 6)
# print('-=-' * 20)
import datetime
segurado = {'nome': str(input('Nome: ')), 'idade': abs(int(input('Ano de nascimento: ')) - datetime.date.today().year)}
a = int(input('Carteira de trabalho (0 não tem): '))
segurado['ctps'] = a
if a > 0:
    segurado['contratação'] = int(input('Ano de contração: '))
    segurado['salário'] = float(input('Salário: '))
    segurado['aposentadoria'] = segurado['idade'] + ((segurado['contratação'] + 35) - datetime.date.today().year)
for k, v in segurado.items():
    print(f'{k} tem o valor {v}')







