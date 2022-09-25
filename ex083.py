# print('=' * 6, 'DESAFIO 83/AULA17', '=' * 6)
# print('-=-' * 20)
expr = str(input('Digite uma expressão numérica: '))
list_1 = list(expr)
a = list_1.count('(')
b = list_1.count(')')
if a == b:
    print('Sua expresão está correta!')
else:
    print('Sua expresão está errada!')
    if a - b > 0:
        print(f'Falta {abs(a-b)} parêntese(s) à direita!')
    else:
        print(f'Falta {abs(a-b)} parêntese(s) à esquerda!')
